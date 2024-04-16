import logging
import warnings
from inspect import Parameter
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Type,
    Union,
)

import nats
from nats.aio.client import (
    DEFAULT_CONNECT_TIMEOUT,
    DEFAULT_DRAIN_TIMEOUT,
    DEFAULT_INBOX_PREFIX,
    DEFAULT_MAX_FLUSHER_QUEUE_SIZE,
    DEFAULT_MAX_OUTSTANDING_PINGS,
    DEFAULT_MAX_RECONNECT_ATTEMPTS,
    DEFAULT_PENDING_SIZE,
    DEFAULT_PING_INTERVAL,
    DEFAULT_RECONNECT_TIME_WAIT,
)
from nats.errors import Error
from nats.js.errors import BadRequestError
from typing_extensions import Annotated, Doc, override

from faststream.__about__ import SERVICE_NAME
from faststream.broker.message import gen_cor_id
from faststream.nats.broker.logging import NatsLoggingBroker
from faststream.nats.broker.registrator import NatsRegistrator
from faststream.nats.publisher.producer import NatsFastProducer, NatsJSFastProducer
from faststream.nats.security import parse_security
from faststream.nats.subscriber.asyncapi import AsyncAPISubscriber

if TYPE_CHECKING:
    import ssl
    from types import TracebackType

    from fast_depends.dependencies import Depends
    from nats.aio.client import (
        Callback,
        Client,
        Credentials,
        ErrorCallback,
        JWTCallback,
        SignatureCallback,
    )
    from nats.aio.msg import Msg
    from nats.js.client import JetStreamContext
    from typing_extensions import TypedDict, Unpack

    from faststream.asyncapi import schema as asyncapi
    from faststream.broker.publisher.proto import ProducerProto
    from faststream.broker.types import (
        BrokerMiddleware,
        CustomCallable,
    )
    from faststream.nats.publisher.asyncapi import AsyncAPIPublisher
    from faststream.security import BaseSecurity
    from faststream.types import (
        AnyDict,
        DecodedMessage,
        Decorator,
        LoggerProto,
        SendableMessage,
    )

    class NatsInitKwargs(TypedDict, total=False):
        """NatsBroker.connect() method type hints."""

        error_cb: Annotated[
            Optional["ErrorCallback"],
            Doc("Callback to report errors."),
        ]
        disconnected_cb: Annotated[
            Optional["Callback"],
            Doc("Callback to report disconnection from NATS."),
        ]
        closed_cb: Annotated[
            Optional["Callback"],
            Doc("Callback to report when client stops reconnection to NATS."),
        ]
        discovered_server_cb: Annotated[
            Optional["Callback"],
            Doc("Callback to report when a new server joins the cluster."),
        ]
        reconnected_cb: Annotated[
            Optional["Callback"], Doc("Callback to report success reconnection.")
        ]
        name: Annotated[
            Optional[str],
            Doc("Label the connection with name (shown in NATS monitoring)."),
        ]
        pedantic: Annotated[
            bool,
            Doc(
                "Turn on NATS server pedantic mode that performs extra checks on the protocol. "
                "https://docs.nats.io/using-nats/developer/connecting/misc#turn-on-pedantic-mode"
            ),
        ]
        verbose: Annotated[
            bool,
            Doc("Verbose mode produce more feedback about code execution."),
        ]
        allow_reconnect: Annotated[
            bool,
            Doc("Whether recover connection automatically or not."),
        ]
        connect_timeout: Annotated[
            int,
            Doc("Timeout in seconds to establish connection with NATS server."),
        ]
        reconnect_time_wait: Annotated[
            int,
            Doc("Time in seconds to wait for reestablish connection to NATS server"),
        ]
        max_reconnect_attempts: Annotated[
            int,
            Doc("Maximum attempts number to reconnect to NATS server."),
        ]
        ping_interval: Annotated[
            int,
            Doc("Interval in seconds to ping."),
        ]
        max_outstanding_pings: Annotated[
            int,
            Doc("Maximum number of failed pings"),
        ]
        dont_randomize: Annotated[
            bool,
            Doc(
                "Boolean indicating should client randomly shuffle servers list for reconnection randomness."
            ),
        ]
        flusher_queue_size: Annotated[
            int, Doc("Max count of commands awaiting to be flushed to the socket")
        ]
        no_echo: Annotated[
            bool,
            Doc("Boolean indicating should commands be echoed."),
        ]
        tls: Annotated[
            Optional["ssl.SSLContext"],
            Doc("Some SSL context to make NATS connections secure."),
        ]
        tls_hostname: Annotated[
            Optional[str],
            Doc("Hostname for TLS."),
        ]
        user: Annotated[
            Optional[str],
            Doc("Username for NATS auth."),
        ]
        password: Annotated[
            Optional[str],
            Doc("Username password for NATS auth."),
        ]
        token: Annotated[
            Optional[str],
            Doc("Auth token for NATS auth."),
        ]
        drain_timeout: Annotated[
            int,
            Doc("Timeout in seconds to drain subscriptions."),
        ]
        signature_cb: Annotated[
            Optional["SignatureCallback"],
            Doc(
                "A callback used to sign a nonce from the server while "
                "authenticating with nkeys. The user should sign the nonce and "
                "return the base64 encoded signature."
            ),
        ]
        user_jwt_cb: Annotated[
            Optional["JWTCallback"],
            Doc(
                "A callback used to fetch and return the account "
                "signed JWT for this user."
            ),
        ]
        user_credentials: Annotated[
            Optional["Credentials"],
            Doc("A user credentials file or tuple of files."),
        ]
        nkeys_seed: Annotated[
            Optional[str],
            Doc("Nkeys seed to be used."),
        ]
        inbox_prefix: Annotated[
            Union[str, bytes],
            Doc(
                "Prefix for generating unique inboxes, subjects with that prefix and NUID.ß"
            ),
        ]
        pending_size: Annotated[
            int,
            Doc("Max size of the pending buffer for publishing commands."),
        ]
        flush_timeout: Annotated[
            Optional[float],
            Doc("Max duration to wait for a forced flush to occur."),
        ]


class NatsBroker(
    NatsRegistrator,
    NatsLoggingBroker,
):
    """A class to represent a NATS broker."""

    url: List[str]
    stream: Optional["JetStreamContext"]

    _producer: Optional["NatsFastProducer"]
    _js_producer: Optional["NatsJSFastProducer"]

    def __init__(
        self,
        servers: Annotated[
            Union[str, Iterable[str]],
            Doc("NATS cluster addresses to connect."),
        ] = ("nats://localhost:4222",),
        *,
        error_cb: Annotated[
            Optional["ErrorCallback"],
            Doc("Callback to report errors."),
        ] = None,
        disconnected_cb: Annotated[
            Optional["Callback"],
            Doc("Callback to report disconnection from NATS."),
        ] = None,
        closed_cb: Annotated[
            Optional["Callback"],
            Doc("Callback to report when client stops reconnection to NATS."),
        ] = None,
        discovered_server_cb: Annotated[
            Optional["Callback"],
            Doc("Callback to report when a new server joins the cluster."),
        ] = None,
        reconnected_cb: Annotated[
            Optional["Callback"], Doc("Callback to report success reconnection.")
        ] = None,
        name: Annotated[
            Optional[str],
            Doc("Label the connection with name (shown in NATS monitoring)."),
        ] = SERVICE_NAME,
        pedantic: Annotated[
            bool,
            Doc(
                "Turn on NATS server pedantic mode that performs extra checks on the protocol. "
                "https://docs.nats.io/using-nats/developer/connecting/misc#turn-on-pedantic-mode"
            ),
        ] = False,
        verbose: Annotated[
            bool,
            Doc("Verbose mode produce more feedback about code execution."),
        ] = False,
        allow_reconnect: Annotated[
            bool,
            Doc("Whether recover connection automatically or not."),
        ] = True,
        connect_timeout: Annotated[
            int,
            Doc("Timeout in seconds to establish connection with NATS server."),
        ] = DEFAULT_CONNECT_TIMEOUT,
        reconnect_time_wait: Annotated[
            int,
            Doc("Time in seconds to wait for reestablish connection to NATS server"),
        ] = DEFAULT_RECONNECT_TIME_WAIT,
        max_reconnect_attempts: Annotated[
            int,
            Doc("Maximum attempts number to reconnect to NATS server."),
        ] = DEFAULT_MAX_RECONNECT_ATTEMPTS,
        ping_interval: Annotated[
            int,
            Doc("Interval in seconds to ping."),
        ] = DEFAULT_PING_INTERVAL,
        max_outstanding_pings: Annotated[
            int,
            Doc("Maximum number of failed pings"),
        ] = DEFAULT_MAX_OUTSTANDING_PINGS,
        dont_randomize: Annotated[
            bool,
            Doc(
                "Boolean indicating should client randomly shuffle servers list for reconnection randomness."
            ),
        ] = False,
        flusher_queue_size: Annotated[
            int, Doc("Max count of commands awaiting to be flushed to the socket")
        ] = DEFAULT_MAX_FLUSHER_QUEUE_SIZE,
        no_echo: Annotated[
            bool,
            Doc("Boolean indicating should commands be echoed."),
        ] = False,
        tls: Annotated[
            Optional["ssl.SSLContext"],
            Doc("Some SSL context to make NATS connections secure."),
        ] = None,
        tls_hostname: Annotated[
            Optional[str],
            Doc("Hostname for TLS."),
        ] = None,
        user: Annotated[
            Optional[str],
            Doc("Username for NATS auth."),
        ] = None,
        password: Annotated[
            Optional[str],
            Doc("Username password for NATS auth."),
        ] = None,
        token: Annotated[
            Optional[str],
            Doc("Auth token for NATS auth."),
        ] = None,
        drain_timeout: Annotated[
            int,
            Doc("Timeout in seconds to drain subscriptions."),
        ] = DEFAULT_DRAIN_TIMEOUT,
        signature_cb: Annotated[
            Optional["SignatureCallback"],
            Doc(
                "A callback used to sign a nonce from the server while "
                "authenticating with nkeys. The user should sign the nonce and "
                "return the base64 encoded signature."
            ),
        ] = None,
        user_jwt_cb: Annotated[
            Optional["JWTCallback"],
            Doc(
                "A callback used to fetch and return the account "
                "signed JWT for this user."
            ),
        ] = None,
        user_credentials: Annotated[
            Optional["Credentials"],
            Doc("A user credentials file or tuple of files."),
        ] = None,
        nkeys_seed: Annotated[
            Optional[str],
            Doc("Nkeys seed to be used."),
        ] = None,
        inbox_prefix: Annotated[
            Union[str, bytes],
            Doc(
                "Prefix for generating unique inboxes, subjects with that prefix and NUID.ß"
            ),
        ] = DEFAULT_INBOX_PREFIX,
        pending_size: Annotated[
            int,
            Doc("Max size of the pending buffer for publishing commands."),
        ] = DEFAULT_PENDING_SIZE,
        flush_timeout: Annotated[
            Optional[float],
            Doc("Max duration to wait for a forced flush to occur."),
        ] = None,
        # broker args
        graceful_timeout: Annotated[
            Optional[float],
            Doc(
                "Graceful shutdown timeout. Broker waits for all running subscribers completion before shut down."
            ),
        ] = None,
        decoder: Annotated[
            Optional["CustomCallable"],
            Doc("Custom decoder object."),
        ] = None,
        parser: Annotated[
            Optional["CustomCallable"],
            Doc("Custom parser object."),
        ] = None,
        dependencies: Annotated[
            Iterable["Depends"],
            Doc("Dependencies to apply to all broker subscribers."),
        ] = (),
        middlewares: Annotated[
            Iterable["BrokerMiddleware[Msg]"],
            Doc("Middlewares to apply to all broker publishers/subscribers."),
        ] = (),
        # AsyncAPI args
        security: Annotated[
            Optional["BaseSecurity"],
            Doc(
                "Security options to connect broker and generate AsyncAPI server security information."
            ),
        ] = None,
        asyncapi_url: Annotated[
            Union[str, Iterable[str], None],
            Doc("AsyncAPI hardcoded server addresses. Use `servers` if not specified."),
        ] = None,
        protocol: Annotated[
            Optional[str],
            Doc("AsyncAPI server protocol."),
        ] = "nats",
        protocol_version: Annotated[
            Optional[str],
            Doc("AsyncAPI server protocol version."),
        ] = "custom",
        description: Annotated[
            Optional[str],
            Doc("AsyncAPI server description."),
        ] = None,
        tags: Annotated[
            Optional[Iterable[Union["asyncapi.Tag", "asyncapi.TagDict"]]],
            Doc("AsyncAPI server tags."),
        ] = None,
        # logging args
        logger: Annotated[
            Union["LoggerProto", None, object],
            Doc("User specified logger to pass into Context and log service messages."),
        ] = Parameter.empty,
        log_level: Annotated[
            int,
            Doc("Service messages log level."),
        ] = logging.INFO,
        log_fmt: Annotated[
            Optional[str],
            Doc("Default logger log format."),
        ] = None,
        # FastDepends args
        apply_types: Annotated[
            bool,
            Doc("Whether to use FastDepends or not."),
        ] = True,
        validate: Annotated[
            bool,
            Doc("Whether to cast types using Pydantic validation."),
        ] = True,
        _get_dependant: Annotated[
            Optional[Callable[..., Any]],
            Doc("Custom library dependant generator callback."),
        ] = None,
        _call_decorators: Annotated[
            Iterable["Decorator"],
            Doc("Any custom decorator to apply to wrapped functions."),
        ] = (),
    ) -> None:
        """Initialize the NatsBroker object."""
        if tls:  # pragma: no cover
            warnings.warn(
                (
                    "\nNATS `tls` option was deprecated and will be removed in 0.6.0"
                    "\nPlease, use `security` with `BaseSecurity` or `SASLPlaintext` instead"
                ),
                DeprecationWarning,
                stacklevel=2,
            )

        if user or password:
            warnings.warn(
                (
                    "\nNATS `user` and `password` options were deprecated and will be removed in 0.6.0"
                    "\nPlease, use `security` with `SASLPlaintext` instead"
                ),
                DeprecationWarning,
                stacklevel=2,
            )

        secure_kwargs = {
            "tls": tls,
            "user": user,
            "password": password,
            **parse_security(security),
        }

        servers = [servers] if isinstance(servers, str) else list(servers)

        if asyncapi_url is not None:
            if isinstance(asyncapi_url, str):
                asyncapi_url = [asyncapi_url]
            else:
                asyncapi_url = list(asyncapi_url)
        else:
            asyncapi_url = servers

        super().__init__(
            # NATS options
            servers=servers,
            name=name,
            verbose=verbose,
            allow_reconnect=allow_reconnect,
            reconnect_time_wait=reconnect_time_wait,
            max_reconnect_attempts=max_reconnect_attempts,
            no_echo=no_echo,
            pedantic=pedantic,
            inbox_prefix=inbox_prefix,
            pending_size=pending_size,
            connect_timeout=connect_timeout,
            drain_timeout=drain_timeout,
            flush_timeout=flush_timeout,
            ping_interval=ping_interval,
            max_outstanding_pings=max_outstanding_pings,
            dont_randomize=dont_randomize,
            flusher_queue_size=flusher_queue_size,
            # security
            tls_hostname=tls_hostname,
            token=token,
            user_credentials=user_credentials,
            nkeys_seed=nkeys_seed,
            **secure_kwargs,
            # callbacks
            error_cb=self._log_connection_broken(error_cb),
            reconnected_cb=self._log_reconnected(reconnected_cb),
            disconnected_cb=disconnected_cb,
            closed_cb=closed_cb,
            discovered_server_cb=discovered_server_cb,
            signature_cb=signature_cb,
            user_jwt_cb=user_jwt_cb,
            # Basic args
            # broker base
            graceful_timeout=graceful_timeout,
            dependencies=dependencies,
            decoder=decoder,
            parser=parser,
            middlewares=middlewares,
            # AsyncAPI
            description=description,
            asyncapi_url=asyncapi_url,
            protocol=protocol,
            protocol_version=protocol_version,
            security=security,
            tags=tags,
            # logging
            logger=logger,
            log_level=log_level,
            log_fmt=log_fmt,
            # FastDepends args
            apply_types=apply_types,
            validate=validate,
            _get_dependant=_get_dependant,
            _call_decorators=_call_decorators,
        )

        self.__is_connected = False
        self._producer = None

        # JS options
        self.stream = None
        self._js_producer = None

    @override
    async def connect(  # type: ignore[override]
        self,
        servers: Annotated[
            Union[str, Iterable[str], object],
            Doc("NATS cluster addresses to connect."),
        ] = Parameter.empty,
        **kwargs: "Unpack[NatsInitKwargs]",
    ) -> "Client":
        """Connect broker object to NATS cluster.

        To startup subscribers too you should use `broker.start()` after/instead this method.
        """
        if servers is not Parameter.empty:
            connect_kwargs: "AnyDict" = {
                **kwargs,
                "servers": servers,
            }
        else:
            connect_kwargs = {**kwargs}

        return await super().connect(**connect_kwargs)

    async def _connect(self, **kwargs: Any) -> "Client":
        self.__is_connected = True
        connection = await nats.connect(**kwargs)

        self._producer = NatsFastProducer(
            connection=connection,
            decoder=self._decoder,
            parser=self._parser,
        )

        stream = self.stream = connection.jetstream()

        self._js_producer = NatsJSFastProducer(
            connection=stream,
            decoder=self._decoder,
            parser=self._parser,
        )

        return connection

    async def _close(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_val: Optional[BaseException] = None,
        exc_tb: Optional["TracebackType"] = None,
    ) -> None:
        self._producer = None
        self._js_producer = None
        self.stream = None

        if self._connection is not None:
            await self._connection.drain()

        await super()._close(exc_type, exc_val, exc_tb)
        self.__is_connected = False

    async def start(self) -> None:
        """Connect broker to NATS cluster and startup all subscribers."""
        await super().start()

        assert self._connection  # nosec B101
        assert self.stream, "Broker should be started already"  # nosec B101
        assert self._producer, "Broker should be started already"  # nosec B101

        # TODO: filter by already running handlers after TestClient refactor
        for handler in self._subscribers.values():
            stream = handler.stream

            log_context = handler.get_log_context(None)

            if stream is not None and stream.declare:
                try:  # pragma: no branch
                    await self.stream.add_stream(
                        config=stream.config,
                        subjects=stream.subjects,
                    )

                except BadRequestError as e:
                    old_config = (await self.stream.stream_info(stream.name)).config

                    if (
                        e.description
                        == "stream name already in use with a different configuration"
                    ):
                        self._log(str(e), logging.WARNING, log_context)
                        await self.stream.update_stream(
                            config=stream.config,
                            subjects=tuple(
                                set(old_config.subjects or ()).union(stream.subjects)
                            ),
                        )

                    else:  # pragma: no cover
                        self._log(str(e), logging.ERROR, log_context, exc_info=e)

                finally:
                    # prevent from double declaration
                    stream.declare = False

            self._log(
                f"`{handler.call_name}` waiting for messages",
                extra=log_context,
            )
            await handler.start()

    @override
    async def publish(  # type: ignore[override]
        self,
        message: Annotated[
            "SendableMessage",
            Doc(
                "Message body to send. "
                "Can be any encodable object (native python types or `pydantic.BaseModel`)."
            ),
        ],
        subject: Annotated[
            str,
            Doc("NATS subject to send message."),
        ],
        headers: Annotated[
            Optional[Dict[str, str]],
            Doc(
                "Message headers to store metainformation. "
                "**content-type** and **correlation_id** will be set automatically by framework anyway."
            ),
        ] = None,
        reply_to: Annotated[
            str,
            Doc("NATS subject name to send response."),
        ] = "",
        correlation_id: Annotated[
            Optional[str],
            Doc(
                "Manual message **correlation_id** setter. "
                "**correlation_id** is a useful option to trace messages."
            ),
        ] = None,
        stream: Annotated[
            Optional[str],
            Doc(
                "This option validates that the target subject is in presented stream. "
                "Can be omitted without any effect."
            ),
        ] = None,
        timeout: Annotated[
            Optional[float],
            Doc("Timeout to send message to NATS."),
        ] = None,
        *,
        rpc: Annotated[
            bool,
            Doc("Whether to wait for reply in blocking mode."),
        ] = False,
        rpc_timeout: Annotated[
            Optional[float],
            Doc("RPC reply waiting time."),
        ] = 30.0,
        raise_timeout: Annotated[
            bool,
            Doc(
                "Whetever to raise `TimeoutError` or return `None` at **rpc_timeout**. "
                "RPC request returns `None` at timeout by default."
            ),
        ] = False,
    ) -> Optional["DecodedMessage"]:
        """Publish message directly.

        This method allows you to publish message in not AsyncAPI-documented way. You can use it in another frameworks
        applications or to publish messages from time to time.

        Please, use `@broker.publisher(...)` or `broker.publisher(...).publish(...)` instead in a regular way.
        """
        publihs_kwargs = {
            "subject": subject,
            "headers": headers,
            "reply_to": reply_to,
            "correlation_id": correlation_id or gen_cor_id(),
            "rpc": rpc,
            "rpc_timeout": rpc_timeout,
            "raise_timeout": raise_timeout,
        }

        producer: Optional[ProducerProto]
        if stream is None:
            producer = self._producer
        else:
            producer = self._js_producer
            publihs_kwargs.update(
                {
                    "stream": stream,
                    "timeout": timeout,
                }
            )

        return await super().publish(
            message,
            producer=producer,
            **publihs_kwargs,
        )

    @override
    def setup_subscriber(  # type: ignore[override]
        self,
        subscriber: "AsyncAPISubscriber",
    ) -> None:
        connection: Union["Client", "JetStreamContext", None] = None

        connection = self._connection if subscriber.stream is None else self.stream

        return super().setup_subscriber(subscriber, connection=connection)

    @override
    def setup_publisher(  # type: ignore[override]
        self,
        publisher: "AsyncAPIPublisher",
    ) -> None:
        producer: Optional[ProducerProto] = None

        if publisher.stream is not None:
            if self._js_producer is not None:
                producer = self._js_producer

        elif self._producer is not None:
            producer = self._producer

        publisher.setup(
            producer=producer,
            **self._publisher_setup_extra,
        )

    def _log_connection_broken(
        self,
        error_cb: Optional["ErrorCallback"] = None,
    ) -> "ErrorCallback":
        c = AsyncAPISubscriber.build_log_context(None, "")

        async def wrapper(err: Exception) -> None:
            if error_cb is not None:
                await error_cb(err)

            if isinstance(err, Error) and self.__is_connected:
                self._log(
                    f"Connection broken with {err!r}", logging.WARNING, c, exc_info=err
                )
                self.__is_connected = False

        return wrapper

    def _log_reconnected(
        self,
        cb: Optional["Callback"] = None,
    ) -> "Callback":
        c = AsyncAPISubscriber.build_log_context(None, "")

        async def wrapper() -> None:
            if cb is not None:
                await cb()

            if not self.__is_connected:
                self._log("Connection established", logging.INFO, c)
                self.__is_connected = True

        return wrapper
