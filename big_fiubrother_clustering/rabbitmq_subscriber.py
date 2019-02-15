import pika

class RabbitMQSubscriber:

    def __init__(self, settings):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=settings['connection_url']))
        self.channel = self.connection.channel()
        self.queue = settings['queue']

    def start(message_callback):
        self.message_callback = message_callback

        self.channel.basic_consume(self.callback,
                                   queue=self.queue,
                                   no_ack=True)

        self.channel.start_consuming()

    def callback(ch, method, properties, body):
        self.message_callback(body)

    def stop(self):
        self.channel.stop_consuming()

    def close(self):
        try:
            self.connection.close()
        except pika.exceptions.ConnectionClosed:
            logging.warning('Connection already closed')