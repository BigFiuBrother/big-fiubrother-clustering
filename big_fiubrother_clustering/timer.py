from datetime import datetime
from time import sleep
import threading
import math

class Timer:
	
	def __init__(self, settings):
        self.interval_time = settings['interval_time']
		self.running = False
        self.thread = threading.Thread(target=self.__start_timer)

    def start(self, time):
        self.start_time = datetime.now()
        self.thread.start()
        self.running = True
        self.thread.join()

    def __start_timer(self):
        sleep(self.interval_time)
        self.running = False

    def is_finished(self):
        return not self.running

    def time_until_finished(self):
        return 0 if self.is_finished() else math.ceil((datetime.now() - self.start_time).total_seconds())