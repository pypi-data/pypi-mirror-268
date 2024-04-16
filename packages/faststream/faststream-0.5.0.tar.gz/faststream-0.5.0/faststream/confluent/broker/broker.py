import logging
from asyncio import AbstractEventLoop
from functools import partial
from inspect import Parameter
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Literal,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
)

from typing_extensions import Annotated, Doc, override

from faststream.__about__ import SERVICE_NAME
from faststream.broker.message import gen_cor_id
from faststream.confluent.broker.logging import KafkaLoggingBroker
from faststream.confluent.broker.registrator import KafkaRegistrator
from faststream.confluent.client import AsyncConfluentProducer, _missing
from faststream.confluent.publisher.producer import AsyncConfluentFastProducer
from faststream.confluent.schemas.params import ConsumerConnectionParams
from faststream.confluent.security import parse_security
from faststream.exceptions import NOT_CONNECTED_YET
from faststream.utils.data import filter_by_dict

if TYPE_CHECKING:
    from types import TracebackType

    from confluent_kafka import Message
    from fast_depends.dependencies import Depends

    from faststream.asyncapi import schema as asyncapi
    from faststream.broker.types import (
        BrokerMiddleware,
        CustomCallable,
    )
    from faststream.security import BaseSecurity
    from faststream.types import (
        AnyDict,
        AsyncFunc,
        Decorator,
        LoggerProto,
        SendableMessage,
    )

Partition = TypeVar("Partition")


class KafkaBroker(
    KafkaRegistrator,
    KafkaLoggingBroker,
):
    url: List[str]
    _producer: Optional[AsyncConfluentFastProducer]

    def __init__(
        self,
        bootstrap_servers: Annotated[
            Union[str, Iterable[str]],
            Doc(
                """
            A `host[:port]` string (or list of `host[:port]` strings) that the consumer should contact to bootstrap
            initial cluster metadata.

            This does not have to be the full node list.
            It just needs to have at least one broker that will respond to a
            Metadata API Request. Default port is 9092.
            """
            ),
        ] = "localhost",
        *,
        # both
        request_timeout_ms: Annotated[
            int,
            Doc("Client request timeout in milliseconds."),
        ] = 40 * 1000,
        retry_backoff_ms: Annotated[
            int,
            Doc(" Milliseconds to backoff when retrying on errors."),
        ] = 100,
        metadata_max_age_ms: Annotated[
            int,
            Doc(
                """
            The period of time in milliseconds after
            which we force a refresh of metadata even if we haven't seen any
            partition leadership changes to proactively discover any new
            brokers or partitions.
            """
            ),
        ] = 5 * 60 * 1000,
        connections_max_idle_ms: Annotated[
            int,
            Doc(
                """
             Close idle connections after the number
            of milliseconds specified by this config. Specifying `None` will
            disable idle checks.
            """
            ),
        ] = 9 * 60 * 1000,
        sasl_kerberos_service_name: str = "kafka",
        sasl_kerberos_domain_name: Optional[str] = None,
        sasl_oauth_token_provider: Annotated[
            Optional[str], Doc("OAuthBearer token provider.")
        ] = None,
        loop: Optional[AbstractEventLoop] = None,
        client_id: Annotated[
            Optional[str],
            Doc(
                """
            A name for this client. This string is passed in
            each request to servers and can be used to identify specific
            server-side log entries that correspond to this client. Also
            submitted to :class:`~.consumer.group_coordinator.GroupCoordinator`
            for logging with respect to consumer group administration.
            """
            ),
        ] = SERVICE_NAME,
        # publisher args
        acks: Annotated[
            Union[Literal[0, 1, -1, "all"], object],
            Doc(
                """
            One of ``0``, ``1``, ``all``. The number of acknowledgments
            the producer requires the leader to have received before considering a
            request complete. This controls the durability of records that are
            sent. The following settings are common:

            * ``0``: Producer will not wait for any acknowledgment from the server
              at all. The message will immediately be added to the socket
              buffer and considered sent. No guarantee can be made that the
              server has received the record in this case, and the retries
              configuration will not take effect (as the client won't
              generally know of any failures). The offset given back for each
              record will always be set to -1.
            * ``1``: The broker leader will write the record to its local log but
              will respond without awaiting full acknowledgement from all
              followers. In this case should the leader fail immediately
              after acknowledging the record but before the followers have
              replicated it then the record will be lost.
            * ``all``: The broker leader will wait for the full set of in-sync
              replicas to acknowledge the record. This guarantees that the
              record will not be lost as long as at least one in-sync replica
              remains alive. This is the strongest available guarantee.

            If unset, defaults to ``acks=1``. If `enable_idempotence` is
            :data:`True` defaults to ``acks=all``.
            """
            ),
        ] = _missing,
        key_serializer: Annotated[
            Optional[Callable[[Any], bytes]],
            Doc("Used to convert user-supplied keys to bytes."),
        ] = None,
        value_serializer: Annotated[
            Optional[Callable[[Any], bytes]],
            Doc("used to convert user-supplied message values to bytes."),
        ] = None,
        compression_type: Annotated[
            Optional[Literal["gzip", "snappy", "lz4", "zstd"]],
            Doc(
                """
            The compression type for all data generated bythe producer.
            Compression is of full batches of data, so the efficacy of batching
            will also impact the compression ratio (more batching means better
            compression).
            """
            ),
        ] = None,
        max_batch_size: Annotated[
            int,
            Doc(
                """
            Maximum size of buffered data per partition.
            After this amount `send` coroutine will block until batch is drained.
            """
            ),
        ] = 16 * 1024,
        partitioner: Annotated[
            Union[
                str,
                Callable[
                    [bytes, List[Partition], List[Partition]],
                    Partition,
                ],
            ],
            Doc(
                """
            Callable used to determine which partition
            each message is assigned to. Called (after key serialization):
            ``partitioner(key_bytes, all_partitions, available_partitions)``.
            The default partitioner implementation hashes each non-None key
            using the same murmur2 algorithm as the Java client so that
            messages with the same key are assigned to the same partition.
            When a key is :data:`None`, the message is delivered to a random partition
            (filtered to partitions with available leaders only, if possible).
            """
            ),
        ] = "consistent_random",
        max_request_size: Annotated[
            int,
            Doc(
                """
            The maximum size of a request. This is also
            effectively a cap on the maximum record size. Note that the server
            has its own cap on record size which may be different from this.
            This setting will limit the number of record batches the producer
            will send in a single request to avoid sending huge requests.
            """
            ),
        ] = 1024 * 1024,
        linger_ms: Annotated[
            int,
            Doc(
                """
            The producer groups together any records that arrive
            in between request transmissions into a single batched request.
            Normally this occurs only under load when records arrive faster
            than they can be sent out. However in some circumstances the client
            may want to reduce the number of requests even under moderate load.
            This setting accomplishes this by adding a small amount of
            artificial delay; that is, if first request is processed faster,
            than `linger_ms`, producer will wait ``linger_ms - process_time``.
            """
            ),
        ] = 0,
        send_backoff_ms: int = 100,
        enable_idempotence: Annotated[
            bool,
            Doc(
                """
            When set to `True`, the producer will
            ensure that exactly one copy of each message is written in the
            stream. If `False`, producer retries due to broker failures,
            etc., may write duplicates of the retried message in the stream.
            Note that enabling idempotence acks to set to ``all``. If it is not
            explicitly set by the user it will be chosen.
            """
            ),
        ] = False,
        transactional_id: Optional[str] = None,
        transaction_timeout_ms: int = 60 * 1000,
        # broker base args
        graceful_timeout: Annotated[
            Optional[float],
            Doc(
                "Graceful shutdown timeout. Broker waits for all running subscribers completion before shut down."
            ),
        ] = 15.0,
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
            Iterable[
                Union[
                    "BrokerMiddleware[Message]",
                    "BrokerMiddleware[Tuple[Message, ...]]",
                ]
            ],
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
        ] = None,
        protocol_version: Annotated[
            Optional[str],
            Doc("AsyncAPI server protocol version."),
        ] = "auto",
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
        if protocol is None:
            if security is not None and security.use_ssl:
                protocol = "kafka-secure"
            else:
                protocol = "kafka"

        servers = (
            [bootstrap_servers]
            if isinstance(bootstrap_servers, str)
            else list(bootstrap_servers)
        )

        if asyncapi_url is not None:
            if isinstance(asyncapi_url, str):
                asyncapi_url = [asyncapi_url]
            else:
                asyncapi_url = list(asyncapi_url)
        else:
            asyncapi_url = servers

        super().__init__(
            bootstrap_servers=servers,
            # both args
            client_id=client_id,
            api_version=protocol_version,
            request_timeout_ms=request_timeout_ms,
            retry_backoff_ms=retry_backoff_ms,
            metadata_max_age_ms=metadata_max_age_ms,
            connections_max_idle_ms=connections_max_idle_ms,
            sasl_kerberos_service_name=sasl_kerberos_service_name,
            sasl_kerberos_domain_name=sasl_kerberos_domain_name,
            sasl_oauth_token_provider=sasl_oauth_token_provider,
            loop=loop,
            # publisher args
            acks=acks,
            key_serializer=key_serializer,
            value_serializer=value_serializer,
            compression_type=compression_type,
            max_batch_size=max_batch_size,
            partitioner=partitioner,
            max_request_size=max_request_size,
            linger_ms=linger_ms,
            send_backoff_ms=send_backoff_ms,
            enable_idempotence=enable_idempotence,
            transactional_id=transactional_id,
            transaction_timeout_ms=transaction_timeout_ms,
            # Basic args
            graceful_timeout=graceful_timeout,
            dependencies=dependencies,
            decoder=decoder,
            parser=parser,
            middlewares=middlewares,
            # AsyncAPI args
            description=description,
            asyncapi_url=asyncapi_url,
            protocol=protocol,
            protocol_version=protocol_version,
            security=security,
            tags=tags,
            # Logging args
            logger=logger,
            log_level=log_level,
            log_fmt=log_fmt,
            # FastDepends args
            _get_dependant=_get_dependant,
            _call_decorators=_call_decorators,
            apply_types=apply_types,
            validate=validate,
        )
        self.client_id = client_id
        self._producer = None

    async def _close(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_val: Optional[BaseException] = None,
        exc_tb: Optional["TracebackType"] = None,
    ) -> None:
        if self._producer is not None:  # pragma: no branch
            await self._producer.stop()
            self._producer = None

        await super()._close(exc_type, exc_val, exc_tb)

    async def connect(
        self,
        bootstrap_servers: Annotated[
            Union[str, Iterable[str], object],
            Doc("Kafka addresses to connect."),
        ] = Parameter.empty,
        **kwargs: Any,
    ) -> ConsumerConnectionParams:
        if bootstrap_servers is not Parameter.empty:
            kwargs["bootstrap_servers"] = bootstrap_servers

        return await super().connect(**kwargs)

    @override
    async def _connect(  # type: ignore[override]
        self,
        *,
        client_id: str,
        **kwargs: Any,
    ) -> ConsumerConnectionParams:
        security_params = parse_security(self.security)
        producer = AsyncConfluentProducer(
            **kwargs,
            **security_params,
            client_id=client_id,
        )
        self._producer = AsyncConfluentFastProducer(
            producer=producer,
        )
        return filter_by_dict(ConsumerConnectionParams, {**kwargs, **security_params})

    async def start(self) -> None:
        await super().start()

        for handler in self._subscribers.values():
            self._log(
                f"`{handler.call_name}` waiting for messages",
                extra=handler.get_log_context(None),
            )
            await handler.start()

    @property
    def _subscriber_setup_extra(self) -> "AnyDict":
        return {"client_id": self.client_id, "connection_data": self._connection or {}}

    @override
    async def publish(  # type: ignore[override]
        self,
        message: "SendableMessage",
        topic: str,
        key: Optional[bytes] = None,
        partition: Optional[int] = None,
        timestamp_ms: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
        correlation_id: Optional[str] = None,
        *,
        reply_to: str = "",
        # extra options to be compatible with test client
        **kwargs: Any,
    ) -> Optional[Any]:
        correlation_id = correlation_id or gen_cor_id()

        return await super().publish(
            message,
            producer=self._producer,
            topic=topic,
            key=key,
            partition=partition,
            timestamp_ms=timestamp_ms,
            headers=headers,
            correlation_id=correlation_id,
            reply_to=reply_to,
            **kwargs,
        )

    async def publish_batch(
        self,
        *msgs: "SendableMessage",
        topic: str,
        partition: Optional[int] = None,
        timestamp_ms: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
        reply_to: str = "",
        correlation_id: Optional[str] = None,
    ) -> None:
        assert self._producer, NOT_CONNECTED_YET  # nosec B101

        correlation_id = correlation_id or gen_cor_id()

        call: "AsyncFunc" = self._producer.publish_batch
        for m in self._middlewares:
            call = partial(m(None).publish_scope, call)

        await call(
            *msgs,
            topic=topic,
            partition=partition,
            timestamp_ms=timestamp_ms,
            headers=headers,
            reply_to=reply_to,
            correlation_id=correlation_id,
        )
