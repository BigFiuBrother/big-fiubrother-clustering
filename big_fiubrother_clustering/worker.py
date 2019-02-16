from big_fiubrother_core import SignalHandler
from big_fiubrother_clustering import *
from queue import Queue

class Worker:

    def __init__(self, settings):
        self.subscriber_client = RabbitMQSubscriber(settings['rabbitmq_subscriber_client'])
        self.publisher_client = RabbitMQPublisher(settings['rabbitmq_publisher_client'])
        self.signal_handler = SignalHandler(self.__stop_threads)
        self.thread_queue = Queue()

        self.clustering_thread = ClusteringThread(self.thread_queue, self.publisher_client, settings['clustering'])

        self.listener_threads = []

        for _ in settings['listener_threads']:
            thread = ListenerThread(self.subscriber_client, self.thread_queue)
            self.listener_threads.append(thread)

    def run(self):
        print('[*] Starting clustering worker')
        
        self.clustering_thread.start()

        for thread in self.listener_threads:
            thread.start()

        for thread in self.listener_threads:
            thread.join()

        self.clustering_thread.join()

        self.subscriber_client.close()
        self.publisher_client.close()

    def __stop_threads(self):
        print('[*] Stopping clustering worker')

        for thread in self.listener_threads:
            thread.stop()

        self.clustering_thread.stop()

if __name__ == "__main__":
    print('[*] Configuring clustering worker')

    with open('config.yml') as config_file:
        settings = yaml.load(config_file)

    worker = Worker(settings)

    worker.run()