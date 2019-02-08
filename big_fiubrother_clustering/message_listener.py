class MessageListener:

    def __init__(self, message_client, queue):
        self.message_client = message_client
        self.queue = queue

    def start(self):
        self.message_client.start(self.process)

    def process(self, message):
        queue.put(message)

    def stop(self)
        self.message_client.stop()