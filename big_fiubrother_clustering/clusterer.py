import hdbscan

class Clusterer:

	def __init__(self, settings):
       self.jobs = settings['jobs']
       self.metric = settings['metric']
       self.min_cluster_size = settings['min_cluster_size']
       self.min_samples = settings['min_samples']

    def analyse(self, batch):
        #TODO: Check batch size
        
        clusterer = hdbscan.HDBSCAN(metric=self.metric, 
                                    core_dist_n_jobs=self.jobs,
                                    min_cluster_size=self.min_cluster_size,
                                    min_samples=self.min_samples)

        clusterer.fit(batch)

        #TODO: Create clustering result