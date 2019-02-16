from big_fiubrother_clustering import Face
import threading

class ListenerThread:

    def __init__(self, input_queue, output_queue):
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.thread = threading.Thread(target=self.__start)

    def start(self):
        self.thread.start()
        self.thread.join()

    def __start(self):
        self.input_queue.start(self.__forward_message)

    def __forward_message(self, message):
        unknown_face_message = message.decode()
        face = Face(unknown_face_message.id, unknown_face_message.face_embedding)
        self.output_queue.put(face)

    def stop(self):
        self.input_queue.stop()