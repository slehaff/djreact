'Docstring'
import socket
# import pickle

IP = '192.168.0.50'
PORT = 5005


def collect_mess():
    'Docstring'
    message = b'3singlecos'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message, (IP, PORT))
    return
