# -*- encoding: utf-8 -*-
import logging
import os
import typing
from typing import List  # noqa:F401
from typing import Optional  # noqa:F401
from typing import Type  # noqa:F401
from typing import Union  # noqa:F401

import attr

import ddtrace
from ddtrace.internal import agent
from ddtrace.internal import atexit
from ddtrace.internal import forksafe
from ddtrace.internal import service
from ddtrace.internal import uwsgi
from ddtrace.internal import writer
from ddtrace.internal.datadog.profiling import ddup
from ddtrace.internal.module import ModuleWatchdog
from ddtrace.profiling import collector
from ddtrace.profiling import exporter  # noqa:F401
from ddtrace.profiling import recorder
from ddtrace.profiling import scheduler
from ddtrace.profiling.collector import asyncio
from ddtrace.profiling.collector import memalloc
from ddtrace.profiling.collector import stack
from ddtrace.profiling.collector import stack_event
from ddtrace.profiling.collector import threading
from ddtrace.settings.profiling import config


LOG = logging.getLogger(__name__)


class Profiler(object):
    """Run profiling while code is executed.

    Note that the whole Python process is profiled, not only the code executed. Data from all running threads are
    caught.

    """

    def __init__(self, *args, **kwargs):
        self._profiler = _ProfilerInstance(*args, **kwargs)

    def start(self, stop_on_exit=True, profile_children=True):
        """Start the profiler.

        :param stop_on_exit: Whether to stop the profiler and flush the profile on exit.
        :param profile_children: Whether to start a profiler in child processes.
        """

        if profile_children:
            try:
                uwsgi.check_uwsgi(self._restart_on_fork, atexit=self.stop if stop_on_exit else None)
            except uwsgi.uWSGIMasterProcess:
                # Do nothing, the start() method will be called in each worker subprocess
                return

        self._profiler.start()

        if stop_on_exit:
            atexit.register(self.stop)

        if profile_children:
            forksafe.register(self._restart_on_fork)

    def stop(self, flush=True):
        """Stop the profiler.

        :param flush: Flush last profile.
        """
        atexit.unregister(self.stop)
        try:
            self._profiler.stop(flush)
        except service.ServiceStatusError:
            # Not a best practice, but for backward API compatibility that allowed to call `stop` multiple times.
            pass

    def _restart_on_fork(self):
        # Be sure to stop the parent first, since it might have to e.g. unpatch functions
        # Do not flush data as we don't want to have multiple copies of the parent profile exported.
        try:
            self._profiler.stop(flush=False, join=False)
        except service.ServiceStatusError:
            # This can happen in uWSGI mode: the children won't have the _profiler started from the master process
            pass
        self._profiler = self._profiler.copy()
        self._profiler.start()

    def __getattr__(
        self,
        key,  # type: str
    ):
        # type: (...) -> typing.Any
        return getattr(self._profiler, key)


@attr.s
class _ProfilerInstance(service.Service):
    """A instance of the profiler.

    Each process must manage its own instance.

    """

    # User-supplied values
    url = attr.ib(default=None)
    service = attr.ib(factory=lambda: os.environ.get("DD_SERVICE"))
    tags = attr.ib(factory=dict, type=typing.Dict[str, str])
    env = attr.ib(factory=lambda: os.environ.get("DD_ENV"))
    version = attr.ib(factory=lambda: os.environ.get("DD_VERSION"))
    tracer = attr.ib(default=ddtrace.tracer)
    api_key = attr.ib(factory=lambda: os.environ.get("DD_API_KEY"), type=Optional[str])
    agentless = attr.ib(type=bool, default=config.agentless)
    _memory_collector_enabled = attr.ib(type=bool, default=config.memory.enabled)
    _stack_collector_enabled = attr.ib(type=bool, default=config.stack.enabled)
    _lock_collector_enabled = attr.ib(type=bool, default=config.lock.enabled)
    enable_code_provenance = attr.ib(type=bool, default=config.code_provenance)
    endpoint_collection_enabled = attr.ib(type=bool, default=config.endpoint_collection)

    _recorder = attr.ib(init=False, default=None)
    _collectors = attr.ib(init=False, default=None)
    _collectors_on_import = attr.ib(init=False, default=None, eq=False)
    _scheduler = attr.ib(init=False, default=None, type=Union[scheduler.Scheduler, scheduler.ServerlessScheduler])
    _lambda_function_name = attr.ib(
        init=False, factory=lambda: os.environ.get("AWS_LAMBDA_FUNCTION_NAME"), type=Optional[str]
    )
    _export_libdd_enabled = attr.ib(type=bool, default=config.export.libdd_enabled)
    _export_libdd_required = attr.ib(type=bool, default=config.export.libdd_required)

    ENDPOINT_TEMPLATE = "https://intake.profile.{}"

    def _build_default_exporters(self):
        # type: (...) -> List[exporter.Exporter]
        if not self._export_libdd_enabled:
            # If libdatadog support is enabled, we can skip this part
            _OUTPUT_PPROF = config.output_pprof
            if _OUTPUT_PPROF:
                # DEV: Import this only if needed to avoid importing protobuf
                # unnecessarily
                from ddtrace.profiling.exporter import file

                return [
                    file.PprofFileExporter(prefix=_OUTPUT_PPROF),
                ]

        if self.url is not None:
            endpoint = self.url
        elif self.agentless:
            LOG.warning(
                "Agentless uploading is currently for internal usage only and not officially supported. "
                "You should not enable it unless somebody at Datadog instructed you to do so."
            )
            endpoint = self.ENDPOINT_TEMPLATE.format(os.environ.get("DD_SITE", "datadoghq.com"))
        else:
            if isinstance(self.tracer._writer, writer.AgentWriter):
                endpoint = self.tracer._writer.agent_url
            else:
                endpoint = agent.get_trace_url()

        if self.agentless:
            endpoint_path = "/api/v2/profile"
        else:
            # Agent mode
            # path is relative because it is appended
            # to the agent base path.
            endpoint_path = "profiling/v1/input"

        if self._lambda_function_name is not None:
            self.tags.update({"functionname": self._lambda_function_name})

        # Did the user request the libdd collector?  Better log it.
        if self._export_libdd_enabled:
            LOG.debug("The libdd collector is enabled")
        if self._export_libdd_required:
            LOG.debug("The libdd collector is required")

        # Build the list of enabled Profiling features and send along as a tag
        configured_features = []
        if self._stack_collector_enabled:
            if config.stack.v2.enabled:
                configured_features.append("stack_v2")
            else:
                configured_features.append("stack")
        if self._lock_collector_enabled:
            configured_features.append("lock")
        if self._memory_collector_enabled:
            configured_features.append("mem")
        if config.heap.sample_size > 0:
            configured_features.append("heap")

        if self._export_libdd_enabled:
            configured_features.append("exp_dd")
        else:
            configured_features.append("exp_py")
        if self._export_libdd_required:
            configured_features.append("req_dd")
        configured_features.append("CAP" + str(config.capture_pct))
        configured_features.append("MAXF" + str(config.max_frames))
        self.tags.update({"profiler_config": "_".join(configured_features)})

        endpoint_call_counter_span_processor = self.tracer._endpoint_call_counter_span_processor
        if self.endpoint_collection_enabled:
            endpoint_call_counter_span_processor.enable()

        # If libdd is enabled, then
        # * If initialization fails, disable the libdd collector and fall back to the legacy exporter
        # * If initialization fails and libdd is required, disable everything and return (error)
        if self._export_libdd_enabled:
            try:
                ddup.init(
                    env=self.env,
                    service=self.service,
                    version=self.version,
                    tags=self.tags,  # type: ignore
                    max_nframes=config.max_frames,
                    url=endpoint,
                )
                return []
            except Exception as e:
                LOG.error("Failed to initialize libdd collector (%s), falling back to the legacy collector", e)
                self._export_libdd_enabled = False
                config.export.libdd_enabled = False

                # If we're here and libdd was required, then there's nothing else to do.  We don't have a
                # collector.
                if self._export_libdd_required:
                    LOG.error("libdd collector is required but could not be initialized. Disabling profiling.")
                    config.enabled = False
                    config.export.libdd_required = False
                    config.lock.enabled = False
                    config.memory.enabled = False
                    config.stack.enabled = False
                    return []

        # DEV: Import this only if needed to avoid importing protobuf
        # unnecessarily
        from ddtrace.profiling.exporter import http

        return [
            http.PprofHTTPExporter(
                service=self.service,
                env=self.env,
                tags=self.tags,
                version=self.version,
                api_key=self.api_key,
                endpoint=endpoint,
                endpoint_path=endpoint_path,
                enable_code_provenance=self.enable_code_provenance,
                endpoint_call_counter_span_processor=endpoint_call_counter_span_processor,
            )
        ]

    def __attrs_post_init__(self):
        # type: (...) -> None
        # Allow to store up to 10 threads for 60 seconds at 50 Hz
        max_stack_events = 10 * 60 * 50
        r = self._recorder = recorder.Recorder(
            max_events={
                stack_event.StackSampleEvent: max_stack_events,
                stack_event.StackExceptionSampleEvent: int(max_stack_events / 2),
                # (default buffer size / interval) * export interval
                memalloc.MemoryAllocSampleEvent: int(
                    (memalloc.MemoryCollector._DEFAULT_MAX_EVENTS / memalloc.MemoryCollector._DEFAULT_INTERVAL) * 60
                ),
                # Do not limit the heap sample size as the number of events is relative to allocated memory anyway
                memalloc.MemoryHeapSampleEvent: None,
            },
            default_max_events=config.max_events,
        )

        self._collectors = []

        if self._stack_collector_enabled:
            LOG.debug("Profiling collector (stack) enabled")
            try:
                self._collectors.append(
                    stack.StackCollector(
                        r,
                        tracer=self.tracer,
                        endpoint_collection_enabled=self.endpoint_collection_enabled,
                    )  # type: ignore[call-arg]
                )
                LOG.debug("Profiling collector (stack) initialized")
            except Exception:
                LOG.error("Failed to start stack collector, disabling.", exc_info=True)

        if self._lock_collector_enabled:
            # These collectors require the import of modules, so we create them
            # if their import is detected at runtime.
            def start_collector(collector_class: Type) -> None:
                with self._service_lock:
                    col = collector_class(r, tracer=self.tracer)

                    if self.status == service.ServiceStatus.RUNNING:
                        # The profiler is already running so we need to start the collector
                        try:
                            col.start()
                            LOG.debug("Started collector %r", col)
                        except collector.CollectorUnavailable:
                            LOG.debug("Collector %r is unavailable, disabling", col)
                            return
                        except Exception:
                            LOG.error("Failed to start collector %r, disabling.", col, exc_info=True)
                            return

                    self._collectors.append(col)

            self._collectors_on_import = [
                ("threading", lambda _: start_collector(threading.ThreadingLockCollector)),
                ("asyncio", lambda _: start_collector(asyncio.AsyncioLockCollector)),
            ]

            for module, hook in self._collectors_on_import:
                ModuleWatchdog.register_module_hook(module, hook)

        if self._memory_collector_enabled:
            self._collectors.append(memalloc.MemoryCollector(r))

        exporters = self._build_default_exporters()

        if exporters or self._export_libdd_enabled:
            scheduler_class = (
                scheduler.ServerlessScheduler if self._lambda_function_name else scheduler.Scheduler
            )  # type: (Type[Union[scheduler.Scheduler, scheduler.ServerlessScheduler]])

            self._scheduler = scheduler_class(
                recorder=r,
                exporters=exporters,
                before_flush=self._collectors_snapshot,
            )

    def _collectors_snapshot(self):
        for c in self._collectors:
            try:
                snapshot = c.snapshot()
                if snapshot:
                    for events in snapshot:
                        self._recorder.push_events(events)
            except Exception:
                LOG.error("Error while snapshoting collector %r", c, exc_info=True)

    _COPY_IGNORE_ATTRIBUTES = {"status"}

    def copy(self):
        return self.__class__(
            **{
                a.name: getattr(self, a.name)
                for a in attr.fields(self.__class__)
                if a.name[0] != "_" and a.name not in self._COPY_IGNORE_ATTRIBUTES
            }
        )

    def _start_service(self):
        # type: (...) -> None
        """Start the profiler."""
        collectors = []
        for col in self._collectors:
            try:
                col.start()
            except collector.CollectorUnavailable:
                LOG.debug("Collector %r is unavailable, disabling", col)
            except Exception:
                LOG.error("Failed to start collector %r, disabling.", col, exc_info=True)
            else:
                collectors.append(col)
        self._collectors = collectors

        if self._scheduler is not None:
            self._scheduler.start()

    def _stop_service(self, flush=True, join=True):
        # type: (bool, bool) -> None
        """Stop the profiler.

        :param flush: Flush a last profile.
        """
        # Prevent doing more initialisation now that we are shutting down.
        if self._lock_collector_enabled:
            for module, hook in self._collectors_on_import:
                try:
                    ModuleWatchdog.unregister_module_hook(module, hook)
                except ValueError:
                    pass

        if self._scheduler is not None:
            self._scheduler.stop()
            # Wait for the export to be over: export might need collectors (e.g., for snapshot) so we can't stop
            # collectors before the possibly running flush is finished.
            if join:
                self._scheduler.join()
            if flush:
                # Do not stop the collectors before flushing, they might be needed (snapshot)
                self._scheduler.flush()

        for col in reversed(self._collectors):
            try:
                col.stop()
            except service.ServiceStatusError:
                # It's possible some collector failed to start, ignore failure to stop
                pass

        if join:
            for col in reversed(self._collectors):
                col.join()

    def visible_events(self):
        return not self._export_libdd_enabled
