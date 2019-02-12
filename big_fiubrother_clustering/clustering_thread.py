from big_fiubrother_clustering import Timer, Batch
import queue

class ClusteringThread:

    def __init__(self, input_queue, output_queue, clusterer, settings):
        self.input_queue = input_queue
        self.clusterer = clusterer
        self.output_queue = output_queue
       
        self.timer = Timer(settings['timer'])
        self.batch = Batch(settings['batch'])
        self.running = False

    def start(self):
        self.running = True
        
        while self.running:
            if self.timer.is_finished:
                clustering_result = self.clusterer.analyse(batch)
                if clustering_result.clusters_found:
                    self.output_queue.send(clustering_result)
                self.timer.start()
            else:
                try:
                    unknown_face = self.input_queue.get(timeout=self.timer.time_until_finished())
                    self.batch.add(unknown_face)
                except queue.Empty:
                    pass

    def stop(self):
        self.running = False