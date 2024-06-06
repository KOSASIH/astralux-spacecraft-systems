import socket
import pickle

class CommunicationProtocol:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send_data(self, data):
        # Serialize data using pickle and send over the socket
        serialized_data = pickle.dumps(data)
        self.socket.sendall(serialized_data)

    def receive_data(self):
        # Receive data from the socket and deserialize using pickle
        received_data = self.socket.recv(1024)
        deserialized_data = pickle.loads(received_data)
        return deserialized_data

if __name__ == '__main__':
    protocol = CommunicationProtocol('localhost', 8080)
    data = {'message': 'Hello, Earth!'}
    protocol.send_data(data)
    received_data = protocol.receive_data()
    print("Received data:", received_data)
