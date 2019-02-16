class Face:
	
	def __init__(self, id, embeddings):
        self.id = id
        self.embeddings = embeddings
        self.probability = 0
        self.label = None