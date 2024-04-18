import pika

class MessageQueue(object):
    #region members

    ERR_NOT_CONNECTED = 'not connected to any message queue'

    #endregion
    #region constructor / destructor

    def __init__(self, host: str, port: int, username: str, password: str):
        self.conn = None

        # prepare all connection related parameters
        self.credential = pika.PlainCredentials(username, password)
        self.parameters = pika.ConnectionParameters(host=host, port=port, credentials= self.credential)
        self.channels = []

    def __enter__(self):
        # create a blocking connection
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        del exc_type, exc_value, exc_traceback

        # close all open channels
        for ch in self.channels:
            ch.close()

        # cleanup and close this object
        self.channels.clear()
        self.close()

    #endregion
    #region methods

    def connect(self):
        if not self.conn:
            self.conn = pika.BlockingConnection(self.parameters)

    def close(self):
        if self.conn: self.conn.close()
        self.conn = None

    def publish(self, exchange: str, routing_slip: str, message: str) -> None:

        # check if we have a valid connection
        if not self.conn:
            raise Exception(MessageQueue.ERR_NOT_CONNECTED)

        # create a channel and publish the message
        channel = self.conn.channel()
        channel.basic_publish(exchange=exchange, routing_key=routing_slip, body= message)

        # close the connection
        channel.close()

    def listen(self, exchange_name: str, queue_name: str, binding_key: str,
        event_handler: callable, event_callback_func: str) -> None:

        # check if we have a valid connection
        if not self.conn:
            raise Exception(MessageQueue.ERR_NOT_CONNECTED)

        # create a new channel and add it to our list
        channel = self.conn.channel()
        self.channels.append(channel)

        # setup a queue and make it ready for basic consumption
        channel.queue_declare(queue=queue_name, durable=True, auto_delete=True)
        channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=binding_key)
        channel.basic_consume(
            queue=queue_name,
            auto_ack=True,
            on_message_callback=lambda ch,
            method,
            properties,
            body: getattr(event_handler, event_callback_func)(ch, method, properties, body, binding_key)
        )

        # start listenning
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            pass

        # close everything, remove from list of channels and return
        channel.close()
        self.channels.remove(channel)

    #endregion
