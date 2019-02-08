from big_fiubrother_clustering.pika_subscriber import PikaSubscriber
from big_fiubrother_clustering.message_listener import MessageListener
from queue import Queue
import threading

if __name__ == "__main__":
    print('[*] Configuring big-fiubrother-clustering')

    with open('config.yml') as config_file:
        settings = yaml.load(config_file)


    message_client = PikaSubscriber(settings['message_client'])
    clustering_queue = Queue()

    threads = []

    for i in range(0, settings['listeners']):
        message_listener = MessageListener(message_client, clustering_queue)
        thread = threading.Thread(target=message_listener.start)
        threads.append(thread)
        thread.start()


    
