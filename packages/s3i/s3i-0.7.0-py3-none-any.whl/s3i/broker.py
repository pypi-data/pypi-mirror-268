import asyncio
import functools
import logging
import ssl
import requests
import json

import pika
import pika.exceptions
from pika.adapters.asyncio_connection import AsyncioConnection
from s3i.exception import raise_error_from_s3ib_amqp, raise_error_from_broker_api_response, S3IBrokerRESTError, \
    S3IBrokerAMQPError
from s3i.callback_manager import CallbackManager
from s3i.config import Config

CONTENT_TYPE = "application/json"
HOST = "broker.s3i.vswf.dev"
VIRTUAL_HOST = "s3i"
DIRECT_EXCHANGE = "demo.direct"
EVENT_EXCHANGE = "eventExchange"


class BrokerREST:
    """
    Class Broker REST contains functions to connect to S3I Broker via HTTP REST API, and send and receive messages

    """

    def __init__(self, token, url="https://broker.s3i.vswf.dev/"):
        """
        Constructor

        :param token: Access Token issued from S³I IdentityProvider
        :type token: str
        :param url: url of S³I Broker API
        :type url: str

        """
        self._token = token
        self._url = url
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + self.token}
        self.headers_encrypted = {'Content-Type': 'application/pgp-encrypted',
                                  'Authorization': 'Bearer ' + self.token}

    @property
    def token(self):
        """Returns the JWT currently in use.

        :returns: JWT-Token
        :rtype: str

        """
        return self._token

    @token.setter
    def token(self, new_token):
        """Sets the value of the object's token property to new_token.

        :param new_token: JWT
        :type new_token: str
        """
        self._token = new_token
        self.headers["Authorization"] = "Bearer " + new_token
        self.headers_encrypted["Authorization"] = "Bearer " + new_token

    def send(self, endpoints, msg, encrypted=False):
        """
        Send a S³I-B message via S³I Broker API
        :param endpoints: endpoints of the receivers
        :type endpoints: list of str
        :param msg: message to be sent
        :type msg: str
        :param encrypted: if true, message will be sent encrypted, otherwise not.
        :type encrypted: bool

        """
        if encrypted:
            headers = self.headers_encrypted
        else:
            headers = self.headers
        for endpoint in endpoints:
            response = requests.post(url="{}/{}".format(self._url, endpoint), headers=headers, data=msg)
            raise (response, S3IBrokerRESTError, 201)
        return True

    def receive_once(self, queue):
        """
        Receive one S3I-B message and do not wait for more messages.

        :param queue: queue which starts a listener in order to receive a single message
        :type queue: str
        :return: received S3I-B message
        :rtype: dict
        """

        url = "{}{}".format(self._url, queue)
        response = requests.get(url=url, headers=self.headers)
        raise_error_from_broker_api_response(response, S3IBrokerRESTError, 200)
        return response.json()


class BrokerAMQP:
    _ON_CONNECTION_OPEN = "_on_connection_open"
    _ON_CONNECTION_CLOSED = "_on_connection_closed"
    _ON_CHANNEL_OPEN = "_on_channel_open"
    _ON_CHANNEL_CLOSED = "_on_channel_closed"

    def __init__(self, token, loop=asyncio.get_event_loop(), logger=logging.getLogger()):
        self.__token = token

        self.__connection = None
        self.__channel = None

        self.__loop = loop
        self.__logger = logger

        self.__delivery_tag = 0
        self.__consumer_tag = None
        self.__is_consuming = False

        self.__callback_manager = CallbackManager()

    @property
    def token(self):
        return self.__token

    @property
    def connection(self):
        return self.__connection

    @property
    def channel(self):
        return self.__channel

    @property
    def delivery_tag(self):
        return self.__delivery_tag

    def connect(self):
        credentials = pika.PlainCredentials(
            username=" ",
            password=self.__token,
            erase_on_connect=True
        )
        connection_parameters = pika.ConnectionParameters(
            host=HOST,
            virtual_host=VIRTUAL_HOST,
            credentials=credentials,
            heartbeat=10,
            port=5671,
            ssl_options=pika.SSLOptions(ssl.SSLContext())
        )
        AsyncioConnection(
            parameters=connection_parameters,
            on_open_callback=self.on_connection_open,
            on_open_error_callback=self.on_connection_open_error,
            on_close_callback=self.on_connection_closed,
            custom_ioloop=self.__loop
        )

    def reconnect_token_expired(self, token):
        self.__token = token
        self.__connection.update_secret(token, reason="Token expired")

    def on_connection_open(self, _unused_connection):
        self.__logger.info("[S3I]: Opening broker connection succeed")
        self.__connection = _unused_connection

        _unused_connection.channel(
            on_open_callback=self.on_channel_open
        )

        self.__callback_manager.process(
            self._ON_CONNECTION_OPEN,
            self.__loop
        )

    def on_connection_open_error(self, _unused_connection, err):
        self.__logger.error("[S3I]: Opening broker connection failed: {}".format(err))

    def on_connection_closed(self, _unused_connection, err):
        self.__logger.info("[S3I]: Current Broker connection closed: {}".format(err))

    def on_channel_open(self, _unused_channel):
        self.__logger.info("[S3I]: Opening broker channel succeed")
        self.__channel = _unused_channel

        # Add callback function for channel closing
        _unused_channel.add_on_close_callback(self.on_channel_closed)
        _unused_channel.basic_qos(
            prefetch_count=1
        )

        self.__callback_manager.process(self._ON_CHANNEL_OPEN, self.__loop)

    def on_channel_closed(self, channel, reason):
        self.__logger.info("[S3I]: Current broker channel closed: {}".format(reason))
        self.__callback_manager.process(self._ON_CHANNEL_CLOSED, self.__loop)
        if not self.__connection.is_closed:
            self.__connection.close()

    def add_on_channel_open_callback(self, callback, one_shot, *args, **kwargs):
        self.__callback_manager.add(
            self._ON_CHANNEL_OPEN,
            callback,
            one_shot,
            False,
            *args,
            **kwargs
        )

    def add_on_channel_close_callback(self, callback, one_shot, *arg, **kwargs):
        self.__callback_manager.add(
            self._ON_CHANNEL_CLOSED,
            callback,
            one_shot,
            False,
            *arg,
            **kwargs
        )

    def add_on_connection_open_callback(self, callback, one_shot, *args, **kwargs):
        self.__callback_manager.add(
            self._ON_CONNECTION_OPEN,
            callback,
            one_shot,
            False,
            *args,
            **kwargs
        )

    def add_on_connection_close_callback(self, callback, one_shot, *args, **kwargs):
        self.__callback_manager.add(
            self._ON_CONNECTION_CLOSED,
            callback,
            one_shot,
            False,
            *args,
            **kwargs
        )

    def start_consuming(self, endpoint, on_message):
        self.__consumer_tag = self.__channel.basic_consume(
            auto_ack=True,
            exclusive=True,
            queue=endpoint,
            on_message_callback=on_message
        )
        self.__logger.info(f"Consuming to endpoint {endpoint}")
        self.__is_consuming = True

    def stop_consuming(self):
        cb = functools.partial(
            self.on_consumer_cancel_ok, userdata=self.__consumer_tag
        )
        self.__channel.basic_cancel(self.__consumer_tag, cb)
        self.__is_consuming = False

    def on_consumer_cancel_ok(self, _unused_frame, userdata):
        if not self.__is_consuming:
            self.__channel.close()

    def publish_message(self, endpoint: str, message: dict):
        msg_id = message.get("identifier")
        if isinstance(message, dict):
            message = json.dumps(message)
        self.__delivery_tag += 1
        raise_error_from_s3ib_amqp(
            self.__channel.basic_publish,
            S3IBrokerAMQPError,
            DIRECT_EXCHANGE,
            endpoint,
            message,
            pika.BasicProperties(
                content_type="application/json",
                delivery_mode=pika.DeliveryMode.Transient
            )
        )
        self.__logger.info(f"Sending normal message (message id: {msg_id}, delivery tag: {self.__delivery_tag}) to {endpoint}")

    def publish_event(self, topic, message):
        msg_id = message.get("identifier")
        if isinstance(message, dict):
            message = json.dumps(message)
        self.__delivery_tag += 1
        raise_error_from_s3ib_amqp(
            self.__channel.basic_publish,
            S3IBrokerAMQPError,
            EVENT_EXCHANGE,
            topic,
            message,
            pika.BasicProperties(
                content_type="application/json",
                delivery_mode=pika.DeliveryMode.Transient
            )
        )
        self.__logger.info(f"Sending event message (message id: {msg_id}, delivery tag: {self.__delivery_tag}) to {topic}")


    def create_event_queue(self):
        conf = Config(self.__token)
        identifier = self.__endpoint.replace("s3ibs://", '')
        identifier = identifier.replace("s3ib://", '')
        response = conf.create_broker_event_queue(thing_id=identifier, topic=[])
        self.__event_endpoint = response.json()['queue_name']
        return self.__event_endpoint

    def subscribe_topic(self, topic):
        if self.__channel.is_open and self.__event_endpoint is not None:
            raise_error_from_s3ib_amqp(
                self.__channel.queue_bind,
                S3IBrokerAMQPError,
                exchange=EVENT_EXCHANGE,
                queue=self.__event_endpoint,
                routing_key=topic
            )

        else:
            self.__logger.error("[S3I]: No event endpoint configured yet")
            return False

    def unsubscribe_topic(self, topic):
        if self.__channel.is_open and self.__event_endpoint is not None:
            raise_error_from_s3ib_amqp(
                self.__channel.queue_unbind,
                S3IBrokerAMQPError,
                exchange=EVENT_EXCHANGE,
                queue=self.__event_endpoint,
                routing_key=topic
            )
        else:
            self.__logger.error("[S3I]: No event endpoint configured yet")
            return False
