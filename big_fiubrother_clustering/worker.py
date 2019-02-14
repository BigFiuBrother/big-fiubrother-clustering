from big_fiubrother_clustering import *
from queue import Queue

class Worker:

    def __init__(self, settings):
        self.subscriber_client = RabbitMQSubscriber(settings['rabbitmq_subscriber_client'])
        self.publisher_client = RabbitMQPublisher(settings['rabbitmq_publisher_client'])
        self.thread_queue = Queue()

        self.clustering_thread = ClusteringThread(self.thread_queue, self.publisher_client, settings['clustering'])

        self.listener_threads = []

        for i in settings['listener_threads']:
            thread = ListenerThread(self.subscriber_client, self.thread_queue)
            self.listener_threads.append(thread)

    def start(self):
        self.clustering_thread.start()

        for thread in self.listener_threads:
            thread.start()

        for thread in self.listener_threads:
            thread.join()

        self.clustering_thread.join()


if __name__ == "__main__":
    print('[*] Configuring big-fiubrother-clustering')

    with open('config.yml') as config_file:
        settings = yaml.load(config_file)

    worker = Worker(settings)
    worker.start()
    
