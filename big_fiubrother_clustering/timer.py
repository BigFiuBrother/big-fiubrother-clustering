import math
import threading
from time import sleep
from datetime import datetime

class Timer:
	
	def __init__(self, settings):
        self.time_to_wait = settings['interval_time']
		self.running = False
        self.thread = threading.Thread(target=self.__start_timer)

    def is_finished(self):
        return not self.running

    def start(self, time):
        self.start_time = datetime.now()
        self.running = True
        self.thread.start()
        self.thread.join()

    def time_until_finished(self):
        return 0 if self.is_finished() else math.ceil((datetime.now() - self.start_time).total_seconds())

	def __start_timer(self):
        sleep(self.time_to_wait)
        self.running = False