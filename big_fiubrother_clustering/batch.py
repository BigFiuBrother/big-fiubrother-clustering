from collections import deque

class Batch:

    def __init__(self, settings):
        self.max_size = settings['max_size']
        self.batch = deque()

    def add(self, item):
        self.batch.append(item)

        if len(self.batch) > self.max_size:
            self.batch.popleft()

    def is_empty(self):
        len(self.batch) == 0
