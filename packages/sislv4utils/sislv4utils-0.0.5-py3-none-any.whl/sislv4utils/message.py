import pika
from sislv4utils.config import Config

class MessageQueue(object):
    #region members

    ERR_NOT_CONNECTED = 'not connected to any message queue'

    #endregion
    
    #region methods

    def __init__(self, cf: Config):
        self.conn = None

        # prepare all connection related parameters
        self._credential = pika.PlainCredentials(cf.appuser, cf.apppass)
        self._parameters = pika.ConnectionParameters(host=cf.mq_host, 
            port=cf.mq_port, credentials= self._credential)

    def __enter__(self):
        # create a blocking connection
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        del exc_type, exc_value, exc_traceback
        self.close()

    # connect to the message bus
    def connect(self) ->None:
        if not self.conn:
            self.conn = pika.BlockingConnection(self._parameters)

    # disconnect from the bus
    def close(self) ->None:
        if self.conn: self.conn.close()
        self.conn = None

    # publish a message
    def publish(self, exchange: str, routing_slip: str, message: str) -> None:

        # check if we have a valid connection
        if not self.conn:
            raise Exception(MessageQueue.ERR_NOT_CONNECTED)

        # create a channel and publish the message
        channel = self.conn.channel()
        channel.basic_publish(exchange=exchange, routing_key=routing_slip, body= message)

        # close the connection
        channel.close()

    # listens to a queue
    def listen(self, exchange_name: str, queue_name: str, binding_key: str,
        event_handler: callable, event_callback_func: str) -> None:

        # check if we have a valid connection
        if not self.conn:
            raise Exception(MessageQueue.ERR_NOT_CONNECTED)

        # create a new channel and add it to our list
        channel = self.conn.channel()

        # setup a queue and make it ready for basic consumption
        channel.queue_declare(queue=queue_name, durable=True, auto_delete=True)
        channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=binding_key)
        
        channel.basic_consume(queue=queue_name, auto_ack=True,
            on_message_callback=lambda ch, method, properties,
            body: getattr(event_handler, event_callback_func)(ch, method, properties, body, binding_key)
        )

        # start listenning
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            pass

        # close everything, remove from list of channels and return
        channel.close()

    #endregion
