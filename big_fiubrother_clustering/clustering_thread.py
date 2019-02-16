from big_fiubrother_clustering import *
import threading
import queue

class ClusteringThread:

    def __init__(self, input_queue, output_queue, clusterer, settings):
        self.input_queue = input_queue
        self.output_queue = output_queue
       
        self.clusterer = Clusterer(settings['clusterer'])
        self.timer = Timer(settings['timer'])
        self.batch = Batch(settings['batch'])
        self.running = False

        self.thread = threading.Thread(target=self.__start)

    def start(self):
        self.thread.start()
        self.running = True
        self.thread.join()

    def __start(self):
        while self.running:
            if self.timer.is_finished:
                clusters_message = self.clusterer.analyse(batch)
                if not clusters_message.is_empty:
                    self.output_queue.send(clusters_message)
                self.timer.start()
            else:
                try:
                    unknown_face = self.input_queue.get(timeout=self.timer.time_until_finished())
                    self.batch.add(unknown_face)
                except queue.Empty:
                    pass

    def stop(self):
        self.running = False