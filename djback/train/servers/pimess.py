'Docstring'
import socket
# import pickle

IP = '192.168.0.50'
PORT = 5005


def collect_mess():
    'Message for collecting training data'
    message = b'collect_data'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message, (IP, PORT))
    return
