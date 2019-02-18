from big_fiubrother_core.messages import ClustersMessage
from collections import defaultdict
import numpy as np
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

        clusterer.fit(batch.embeddings)

        new_clusters = defaultdict(list)

        for label, probabilty, face in zip(clusterer.labels_, clusterer.probabilties_, batch.faces):
            if  label >= 0 and probabilty >= face.probabilty:
                face.probabilty = probabilty
                face.label = label
                new_clusters[label].append(face.id)

        return ClustersMessage(list(new_clusters.values()))