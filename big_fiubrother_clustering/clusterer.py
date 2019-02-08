from time import sleep

class Clusterer:

	def __init__(self, queue, settings):
       self.queue = queue
       self.interval_time = settings['interval_time']
       self.max_faces = settings['max_faces']
       self.clustering_jobs = settings['jobs']
       self.current_batch = []

    def start():
        sleep(self.interval_time)

        self.__update_batch()

        clt = DBSCAN(metric='euclidean', n_jobs=self.clustering_jobs)
        clt.fit(encodings)

        #TODO: Inform of groups found
        
    def __update_batch(self):
        queued_faces = self.queue.qsize()
        
        if queued_faces > self.max_faces:
            self.current_batch = []
            faces_to_take = self.max_faces
        else:
            remove_from_batch = len(self.current_batch) + queued_faces - self.max_faces
            if remove_from_batch > 0: 
                del self.current_batch[:queued_faces]
            faces_to_take = queued_faces 

        for i in range(0, faces_to_take):
            self.current_batch.append(self.queue.get())