"Neural net support"
import io
import socket
import struct
import time
import picamera
import pygame
import numpy as np
from pygame.locals import *

SERVER_IP = '192.168.0.22'
SERVER_CONNECTION = 8001


def train_take(connection):
    'text'
    pygame.init()
    WIDTH = 854
    HEIGHT = 480
    windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    i = 0
    max = i+2
    fname = "cosines/" + 'cnncos' + "/" + str(i) + "_saw.jpg"
    print(fname)
    img = pygame.image.load(fname)
    windowSurface.blit(img, (0, 0))
    pygame.display.flip()
    try:
        camera = picamera.PiCamera()
        camera.color_effects = (128, 128)  # turn camera to black and white
        camera.resolution = (640, 480)
        stream = io.BytesIO()
        for foo in camera.capture_continuous(stream, 'png'):
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()
            stream.seek(0)
            connection.write(stream.read())
            i += 1
            if i == max:
                break
            fname = "cosines/" + 'cnncos' + "/" + str(i) + "_saw.jpg"
            print(fname)
            img = pygame.image.load(fname)
            windowSurface.blit(img, (0, 0))
            pygame.display.flip()
            stream.seek(0)
            stream.truncate()
    finally:
        camera.close()
        pygame.quit()


def data_collect():
    'text'
    client_socket = socket.socket()
    client_socket.connect((SERVER_IP, SERVER_CONNECTION))
    connection = client_socket.makefile('wb')
    count = 1000
    j = 0
    while j < count:
        train_take(connection)
        print('Loop count:', j)
        j += 1
    connection.write(struct.pack('<L', 0))
    connection.flush()
    connection.close()
    client_socket.close()
    return
