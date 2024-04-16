import os
import sys
from typing import Iterable

import pymemcache
from pymemcache.client.base import Client
from pymemcache.client.base import PooledClient
from pymemcache.client.hash import HashClient
from pymemcache.exceptions import MemcacheClientError
from pymemcache.exceptions import MemcacheIllegalInputError
from pymemcache.exceptions import MemcacheServerError
from pymemcache.exceptions import MemcacheUnknownCommandError
from pymemcache.exceptions import MemcacheUnknownError

# 3p
from ddtrace import config
from ddtrace.internal.constants import COMPONENT
from ddtrace.vendor import wrapt

# project
from ...constants import ANALYTICS_SAMPLE_RATE_KEY
from ...constants import SPAN_KIND
from ...constants import SPAN_MEASURED_KEY
from ...ext import SpanKind
from ...ext import SpanTypes
from ...ext import db
from ...ext import memcached as memcachedx
from ...ext import net
from ...internal.logger import get_logger
from ...internal.schema import schematize_cache_operation
from ...internal.utils.formats import asbool
from ...pin import Pin


log = get_logger(__name__)


config._add(
    "pymemcache",
    {
        "command_enabled": asbool(os.getenv("DD_TRACE_MEMCACHED_COMMAND_ENABLED", default=False)),
    },
)


# keep a reference to the original unpatched clients
_Client = Client
_HashClient = HashClient


class _WrapperBase(wrapt.ObjectProxy):
    def __init__(self, wrapped_class, *args, **kwargs):
        c = wrapped_class(*args, **kwargs)
        super(_WrapperBase, self).__init__(c)

        # tags to apply to each span generated by this client
        tags = _get_address_tags(*args, **kwargs)

        parent_pin = Pin.get_from(pymemcache)

        if parent_pin:
            pin = parent_pin.clone(tags=tags)
        else:
            pin = Pin(tags=tags)

        # attach the pin onto this instance
        pin.onto(self)

    def _trace_function_as_command(self, func, cmd, *args, **kwargs):
        p = Pin.get_from(self)

        if not p or not p.enabled():
            return func(*args, **kwargs)

        return _trace(func, p, cmd, *args, **kwargs)


class WrappedClient(_WrapperBase):
    """Wrapper providing patched methods of a pymemcache Client.

    Relevant connection information is obtained during initialization and
    attached to each span.

    Keys are tagged in spans for methods that act upon a key.
    """

    def __init__(self, *args, **kwargs):
        super(WrappedClient, self).__init__(_Client, *args, **kwargs)

    def set(self, *args, **kwargs):
        return self._traced_cmd("set", *args, **kwargs)

    def set_many(self, *args, **kwargs):
        return self._traced_cmd("set_many", *args, **kwargs)

    def add(self, *args, **kwargs):
        return self._traced_cmd("add", *args, **kwargs)

    def replace(self, *args, **kwargs):
        return self._traced_cmd("replace", *args, **kwargs)

    def append(self, *args, **kwargs):
        return self._traced_cmd("append", *args, **kwargs)

    def prepend(self, *args, **kwargs):
        return self._traced_cmd("prepend", *args, **kwargs)

    def cas(self, *args, **kwargs):
        return self._traced_cmd("cas", *args, **kwargs)

    def get(self, *args, **kwargs):
        return self._traced_cmd("get", *args, **kwargs)

    def get_many(self, *args, **kwargs):
        return self._traced_cmd("get_many", *args, **kwargs)

    def gets(self, *args, **kwargs):
        return self._traced_cmd("gets", *args, **kwargs)

    def gets_many(self, *args, **kwargs):
        return self._traced_cmd("gets_many", *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self._traced_cmd("delete", *args, **kwargs)

    def delete_many(self, *args, **kwargs):
        return self._traced_cmd("delete_many", *args, **kwargs)

    def incr(self, *args, **kwargs):
        return self._traced_cmd("incr", *args, **kwargs)

    def decr(self, *args, **kwargs):
        return self._traced_cmd("decr", *args, **kwargs)

    def touch(self, *args, **kwargs):
        return self._traced_cmd("touch", *args, **kwargs)

    def stats(self, *args, **kwargs):
        return self._traced_cmd("stats", *args, **kwargs)

    def version(self, *args, **kwargs):
        return self._traced_cmd("version", *args, **kwargs)

    def flush_all(self, *args, **kwargs):
        return self._traced_cmd("flush_all", *args, **kwargs)

    def quit(self, *args, **kwargs):
        return self._traced_cmd("quit", *args, **kwargs)

    def set_multi(self, *args, **kwargs):
        """set_multi is an alias for set_many"""
        return self._traced_cmd("set_many", *args, **kwargs)

    def get_multi(self, *args, **kwargs):
        """set_multi is an alias for set_many"""
        return self._traced_cmd("get_many", *args, **kwargs)

    def _traced_cmd(self, command, *args, **kwargs):
        return self._trace_function_as_command(
            lambda *_args, **_kwargs: getattr(self.__wrapped__, command)(*_args, **_kwargs), command, *args, **kwargs
        )


class WrappedHashClient(_WrapperBase):
    """Wrapper that traces HashClient commands

    This wrapper proxies its command invocations to the underlying HashClient instance.
    When the use_pooling setting is in use, this wrapper starts a span before
    doing the proxy call.

    This is necessary because the use_pooling setting causes Client instances to be
    created and destroyed dynamically in a manner that isn't affected by the
    patch() function.
    """

    def _ensure_traced(self, cmd, key, default_val, *args, **kwargs):
        """
        PooledClient creates Client instances dynamically on request, which means
        those Client instances aren't affected by the wrappers applied in patch().
        We handle this case here by calling trace() before running the command,
        specifically when the client that will be used for the command is a
        PooledClient.

        To avoid double-tracing when the key's client is not a PooledClient, we
        don't create a span and instead rely on patch(). In this case the
        underlying Client instance is long-lived and has been patched already.
        """
        client_for_key = self._get_client(key)
        if isinstance(client_for_key, PooledClient):
            return self._traced_cmd(cmd, client_for_key, key, default_val, *args, **kwargs)
        else:
            return getattr(self.__wrapped__, cmd)(key, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(WrappedHashClient, self).__init__(_HashClient, *args, **kwargs)

    def set(self, key, *args, **kwargs):
        return self._ensure_traced("set", key, False, *args, **kwargs)

    def add(self, key, *args, **kwargs):
        return self._ensure_traced("add", key, False, *args, **kwargs)

    def replace(self, key, *args, **kwargs):
        return self._ensure_traced("replace", key, False, *args, **kwargs)

    def append(self, key, *args, **kwargs):
        return self._ensure_traced("append", key, False, *args, **kwargs)

    def prepend(self, key, *args, **kwargs):
        return self._ensure_traced("prepend", key, False, *args, **kwargs)

    def cas(self, key, *args, **kwargs):
        return self._ensure_traced("cas", key, False, *args, **kwargs)

    def get(self, key, *args, **kwargs):
        return self._ensure_traced("get", key, None, *args, **kwargs)

    def gets(self, key, *args, **kwargs):
        return self._ensure_traced("gets", key, None, *args, **kwargs)

    def delete(self, key, *args, **kwargs):
        return self._ensure_traced("delete", key, False, *args, **kwargs)

    def incr(self, key, *args, **kwargs):
        return self._ensure_traced("incr", key, False, *args, **kwargs)

    def decr(self, key, *args, **kwargs):
        return self._ensure_traced("decr", key, False, *args, **kwargs)

    def touch(self, key, *args, **kwargs):
        return self._ensure_traced("touch", key, False, *args, **kwargs)

    def _traced_cmd(self, command, client, key, default_val, *args, **kwargs):
        # NB this function mimics the logic of HashClient._run_cmd, tracing the call to _safely_run_func
        if client is None:
            return default_val

        args = list(args)
        args.insert(0, key)

        return self._trace_function_as_command(
            lambda *_args, **_kwargs: self._safely_run_func(
                client, getattr(client, command), default_val, *_args, **_kwargs
            ),
            command,
            *args,
            **kwargs,
        )


_HashClient.client_class = WrappedClient


def _get_address_tags(*args, **kwargs):
    """Attempt to get host and port from args passed to Client initializer."""
    tags = {}
    try:
        if len(args):
            host, port = args[0]
            tags[net.TARGET_HOST] = host
            tags[net.TARGET_PORT] = port
    except Exception:
        log.debug("Error collecting client address tags")

    return tags


def _get_query_string(args):
    """Return the query values given the arguments to a pymemcache command.

    If there are multiple query values, they are joined together
    space-separated.
    """
    keys = ""

    # shortcut if no args
    if not args:
        return keys

    # pull out the first arg which will contain any key
    arg = args[0]

    # if we get a dict, convert to list of keys
    if type(arg) is dict:
        arg = list(arg)

    if type(arg) is str:
        keys = arg
    elif type(arg) is bytes:
        keys = arg.decode()
    elif type(arg) is list and len(arg):
        if type(arg[0]) is str:
            keys = " ".join(arg)
        elif type(arg[0]) is bytes:
            keys = b" ".join(arg).decode()

    return keys


def _trace(func, p, method_name, *args, **kwargs):
    """Run and trace the given command.

    Any pymemcache exception is caught and span error information is
    set. The exception is then reraised for the application to handle
    appropriately.

    Relevant tags are set in the span.
    """
    with p.tracer.trace(
        schematize_cache_operation(memcachedx.CMD, cache_provider="memcached"),
        service=p.service,
        resource=method_name,
        span_type=SpanTypes.CACHE,
    ) as span:
        span.set_tag_str(COMPONENT, config.pymemcache.integration_name)
        span.set_tag_str(db.SYSTEM, memcachedx.DBMS_NAME)

        # set span.kind to the type of operation being performed
        span.set_tag_str(SPAN_KIND, SpanKind.CLIENT)

        span.set_tag(SPAN_MEASURED_KEY)
        # set analytics sample rate
        span.set_tag(ANALYTICS_SAMPLE_RATE_KEY, config.pymemcache.get_analytics_sample_rate())

        # try to set relevant tags, catch any exceptions so we don't mess
        # with the application
        try:
            span.set_tags(p.tags)
            if config.pymemcache.command_enabled:
                vals = _get_query_string(args)
                query = "{}{}{}".format(method_name, " " if vals else "", vals)
                span.set_tag_str(memcachedx.QUERY, query)
        except Exception:
            log.debug("Error setting relevant pymemcache tags")

        try:
            result = func(*args, **kwargs)

            if method_name == "get_many" or method_name == "gets_many":
                # gets_many returns a map of key -> (value, cas), else an empty dict if no matches
                # get many returns a map with values, else an empty map if no matches
                span.set_metric(
                    db.ROWCOUNT, sum(1 for doc in result if doc) if result and isinstance(result, Iterable) else 0
                )
            elif method_name == "get":
                # get returns key or None
                span.set_metric(db.ROWCOUNT, 1 if result else 0)
            elif method_name == "gets":
                # gets returns a tuple of (None, None) if key not found, else tuple of (key, index)
                span.set_metric(db.ROWCOUNT, 1 if result[0] else 0)
            return result
        except (
            MemcacheClientError,
            MemcacheServerError,
            MemcacheUnknownCommandError,
            MemcacheUnknownError,
            MemcacheIllegalInputError,
        ):
            (typ, val, tb) = sys.exc_info()
            span.set_exc_info(typ, val, tb)
            raise
