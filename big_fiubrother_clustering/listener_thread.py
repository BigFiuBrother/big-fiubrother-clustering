class ListenerThread:

    def __init__(self, message_client, queue):
        self.message_client = message_client
        self.queue = queue

    def start(self):
        self.message_client.start(self.forward_message)

    def forward_message(self, message):
        queue.put(message)

    def stop(self)
        self.message_client.stop()