import pika

class PikaSubscriber:

    def __init__(self, settings):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=settings['connection_url']))
        self.channel = self.connection.channel()
        self.queue = settings['queue']
        self.processor = processor

    def start(process_callback):
        self.process_callback = process_callback

        self.channel.basic_consume(self.callback,
                                   queue=self.queue,
                                   no_ack=True)

        self.channel.start_consuming()

    def callback(ch, method, properties, body):
        self.process_callback(body)

    def stop(self):
        self.channel.stop_consuming()
        self.connection.close()