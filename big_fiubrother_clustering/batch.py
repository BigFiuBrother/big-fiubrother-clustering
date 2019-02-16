from collections import deque

class Batch:

    def __init__(self, settings):
        self.faces = deque(maxlen=settings['max_size'])
        self.embeddings = deque(maxlen=settings['max_size'])

    def add(self, face):
        self.faces.append(face)
        self.embeddings.append(face.embeddings)

    def is_empty(self):
        len(self.batch) == 0