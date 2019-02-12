class ListenerThread:

    def __init__(self, input_queue, output_queue):
        self.input_queue = input_queue
        self.output_queue = output_queue

    def start(self):
        self.input_queue.start(self.forward_message)

    def forward_message(self, message):
        self.output_queue.put(message)

    def stop(self)
        self.message_client.stop()