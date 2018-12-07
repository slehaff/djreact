import io
import socket
import struct
import time
import picamera
import pygame
import numpy as np
from pygame.locals import *


def capture3cos(cfolder):
    pygame.init()
    WIDTH = 854
    HEIGHT = 480
    windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    client_socket = socket.socket()
    client_socket.connect(('192.168.0.22', 8001))
    connection = client_socket.makefile('wb')
    i = 0
    fname = "cosines/"+ cfolder + "/" + str(i) + "_cos.jpg"
    img = pygame.image.load(fname)
    windowSurface.blit(img, (0, 0))
    pygame.display.flip()
    try:
        camera = picamera.PiCamera()
        camera.color_effects = (128,128) # turn camera to black and white
        camera.resolution = (640, 480)
        time.sleep(.2)
        start = time.time()
        stream = io.BytesIO()
        for foo in camera.capture_continuous(stream, 'png'):
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()
            stream.seek(0)
            connection.write(stream.read())
            i += 1
            if i == 3:
                break
            fname = "cosines/" + cfolder + "/" + str(i) + "_cos.jpg"
            print(fname)
            img = pygame.image.load(fname)
            windowSurface.blit(img, (0, 0))
            pygame.display.flip()
            stream.seek(0)
            stream.truncate()
        connection.write(struct.pack('<L', 0))
    finally:
        camera.close()
        connection.close()
        client_socket.close()
        pygame.quit()


def capt_pro_cos(cfolder):
    pygame.init()
    WIDTH = 854
    HEIGHT = 480
    windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    client_socket = socket.socket()
    client_socket.connect(('192.168.0.22', 8001))
    connection = client_socket.makefile('wb')
    i = 0
    fname = "cosines/"+ cfolder + "/" + str(i) + "_cos.jpg"
    img = pygame.image.load(fname)
    windowSurface.blit(img, (0, 0))
    pygame.display.flip()
    try:
        camera = picamera.PiCamera()
        camera.color_effects = (128,128) # turn camera to black and white
        camera.resolution = (640, 480)
        time.sleep(2)
        start = time.time()
        stream = io.BytesIO()
        for foo in camera.capture_continuous(stream, 'png'):
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()
            stream.seek(0)
            connection.write(stream.read())
            i += 1
            if i == 8:
                break
            fname = "cosines/" + cfolder + "/" + str(i) + "_cos.jpg"
            print(fname)
            img = pygame.image.load(fname)
            windowSurface.blit(img, (0, 0))
            pygame.display.flip()
            stream.seek(0)
            stream.truncate()
        connection.write(struct.pack('<L', 0))
    finally:
        camera.close()
        connection.close()
        client_socket.close()
        pygame.quit()


def cam_cal(cfolder):
    pygame.init()
    WIDTH = 854
    HEIGHT = 480
    windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    client_socket = socket.socket()
    client_socket.connect(('192.168.0.22', 8001))
    connection = client_socket.makefile('wb')
    i = 0
    fname = "cosines/" + 'procal' + "/" + "light.jpg"
    img = pygame.image.load(fname)
    windowSurface.blit(img, (0, 0))
    pygame.display.flip()
    try:
        camera = picamera.PiCamera()
        camera.color_effects = (128,128) # turn camera to black and white
        camera.resolution = (640, 480)
        time.sleep(2)
        start = time.time()
        stream = io.BytesIO()
        for foo in camera.capture_continuous(stream, 'png'):
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()
            stream.seek(0)
            connection.write(stream.read())
            i += 1
            if i == 10:
                break
            stream.seek(0)
            stream.truncate()
        connection.write(struct.pack('<L', 0))
    finally:
        camera.close()
        connection.close()
        client_socket.close()
        pygame.quit()


def texture(cfolder, connection):
    pygame.init()
    WIDTH = 854
    HEIGHT = 480
    windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
 
    fname = "cosines/"+ cfolder + "/" + "texture.png"
    print(fname)
    img = pygame.image.load(fname)
    windowSurface.blit(img, (0, 0))
    pygame.display.flip()
    try:
        camera = picamera.PiCamera()
        camera.shutter_speed = 50000
        camera.resolution = (640, 480)
        stream = io.BytesIO()
        for foo in camera.capture_continuous(stream, 'png'):
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()
            stream.seek(0)
            connection.write(stream.read())
            stream.seek(0)
            stream.truncate()
            break
        # connection.write(struct.pack('<L', 0))
    finally:
        camera.close()
        pygame.quit()
    return


def vertical(cfolder, i, connection):
    pygame.init()
    WIDTH = 854
    HEIGHT = 480
    windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    max = i+3
    fname = "cosines/"+ cfolder + "/" + str(i) + "_cos.jpg"
    print(fname)
    img = pygame.image.load(fname)
    windowSurface.blit(img, (0, 0))
    pygame.display.flip()
    camera = picamera.PiCamera()
    try:
        camera.color_effects = (128,128) # turn camera to black and white
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
            fname = "cosines/" + cfolder + "/" + str(i) + "_cos.jpg"
            print(fname)
            img = pygame.image.load(fname)
            windowSurface.blit(img, (0, 0))
            pygame.display.flip()
            stream.seek(0)
            stream.truncate()
            # connection.write(struct.pack('<L', 0))
    finally:
        camera.close()
        pygame.quit()
    return


def horizontal(cfolder, i, connection):
    pygame.init()
    WIDTH = 854
    HEIGHT = 480
    windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    max = i+3
    fname = "cosines/" + cfolder + "/" + str(i) + "_cos.jpg"
    print(fname)
    img = pygame.image.load(fname)
    windowSurface.blit(img, (0, 0))
    pygame.display.flip()
    try:
        camera = picamera.PiCamera()
        camera.color_effects = (128,128) # turn camera to black and white
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
            fname = "cosines/" + cfolder + "/" + str(i) + "_cos.jpg"
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


def horizontal2(cfolder, i, connection):
    pygame.init()
    WIDTH = 854
    HEIGHT = 480
    windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    max = i+2
    fname = "cosines/" + cfolder + "/" + str(i) + "_cos.jpg"
    print(fname)
    img = pygame.image.load(fname)
    windowSurface.blit(img, (0, 0))
    pygame.display.flip()
    try:
        camera = picamera.PiCamera()
        camera.color_effects = (128,128) # turn camera to black and white
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
            fname = "cosines/" + cfolder + "/" + str(i) + "_cos.jpg"
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


def horizontal4(cfolder, i, connection):
    pygame.init()
    WIDTH = 854
    HEIGHT = 480
    windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    max = i+4
    fname = "cosines/" + cfolder + "/" + str(i) + "_cos.jpg"
    print(fname)
    img = pygame.image.load(fname)
    windowSurface.blit(img, (0, 0))
    pygame.display.flip()
    try:
        camera = picamera.PiCamera()
        camera.color_effects = (128,128) # turn camera to black and white
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
            fname = "cosines/" + cfolder + "/" + str(i) + "_cos.jpg"
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


def scan(cfolder):
    client_socket = socket.socket()
    client_socket.connect(('192.168.0.22', 8001))
    connection = client_socket.makefile('wb')
    texture(cfolder, connection)
    print('horizontal')
    horizontal(cfolder=cfolder, i=0, connection=connection)
    horizontal(cfolder=cfolder, i=6, connection=connection)
    connection.write(struct.pack('<L', 0))
    connection.flush()
    connection.close()
    client_socket.close()
    return


def scan4(cfolder):
    client_socket = socket.socket()
    client_socket.connect(('192.168.0.22', 8001))
    connection = client_socket.makefile('wb')
    print('horizontal')
    horizontal4(cfolder=cfolder, i=0, connection=connection)
    connection.write(struct.pack('<L', 0))
    connection.flush()
    connection.close()
    client_socket.close()
    return


def wilm_cal(cfolder):
    client_socket = socket.socket()
    client_socket.connect(('192.168.0.22', 8001))
    connection = client_socket.makefile('wb')
    j = 0
    while j < 1:
        print('texture')
        texture(cfolder=cfolder, connection=connection)
        print('vertical')
        vertical(cfolder=cfolder, i=3, connection=connection)
        print('horizontal')
        horizontal(cfolder=cfolder, i=0, connection=connection)
        print('vertical')
        vertical(cfolder=cfolder, i=6, connection=connection)
        print('horizontal')
        horizontal(cfolder=cfolder, i=9, connection=connection)
        print(j)
        j += 1
    connection.write(struct.pack('<L', 0))
    connection.flush()
    connection.close()
    client_socket.close()
    return


def abs_scan(cfolder):
    client_socket = socket.socket()
    client_socket.connect(('192.168.0.22', 8001))
    connection = client_socket.makefile('wb')
    j = 0
    while j < 1:
        print('horizontal 4')
        horizontal4(cfolder=cfolder, i=0, connection=connection)
        print('horizontal 2')
        horizontal2(cfolder=cfolder, i=4, connection=connection)
        print('horizontal 2')
        horizontal2(cfolder=cfolder, i=8, connection=connection)
        print(j)
        j += 1
    connection.write(struct.pack('<L', 0))
    connection.flush()
    connection.close()
    client_socket.close()
    return

