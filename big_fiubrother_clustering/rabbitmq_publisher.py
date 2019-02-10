import pika

class RabbitMQPublisher:

    def __init__(self, settings):
        self.host = settings['connection_url']
        self.exchange = settings['exchange'] 
        self.__connect()

    def __connect(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()

    def send(self, message):
        if self.connection.is_closed:
            self.__connect()
            logging.warning('Connection lost, reconning to {} to publish message'.format(self.host))
            
        self.__publish(message)
        logging.info('Published message')

    def __publish(self, message):
        self.channel.basic_publish(exchange=self.exchange,
                                   routing_key='',
                                   body=message)

    def close(self):
        try:
            self.connection.close()
        except pika.exceptions.ConnectionClosed:
            logging.warning('Connection already closed')