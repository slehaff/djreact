"Neural net support"
import io
import socket
import struct
import time
import picamera
import pygame
import numpy as np
from pygame.locals import *


def train_take(connection):
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
    return
