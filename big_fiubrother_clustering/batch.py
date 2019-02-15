from collections import deque

class Batch:

    def __init__(self, settings):
        self.batch = deque(maxlen=settings['max_size'])

    def add(self, item):
        self.batch.append(item)

    def is_empty(self):
        len(self.batch) == 0
