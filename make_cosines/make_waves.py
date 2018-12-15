"This module generates SL patterns"
import math
import cv2
import numpy as np


WIDTH = 1920
HEIGHT = 1080
PERIODS = 1
HFPERIODS = 100


def make_triangle(width, height, hfperiods):
    "This functtion makes a sawtooth wave"
    ima = np.zeros((width, height))
    imaline = np.ones(width)
    raw_inp = np.ones(width)
    for i in range(width):
        raw_inp[i] = 255.0*(hfperiods * i/width -
                            math.trunc(hfperiods * i/width))
        imaline[i] = raw_inp[i]
    for j in range(height):
        ima[:, j] = imaline
    ima = np.transpose(ima)
    cv2.imwrite('make_cosines/1_saw.jpg', ima)


def make_sinusoidal(width, height, wvcount, phi):
    'This function makes a cosine wave'
    ima = np.zeros((width, height))
    imaline = np.ones(width)
    for i in range(width):
        imaline[i] = 255.0*(1.0/2.0 + 1.0/2.0*np.cos(2.0*np.pi *
                                                     (1.0*float(phi)/3.0 + wvcount*float(i)/float(width))))
    print(imaline)
    for j in range(height):
        ima[:, j] = imaline
    ima = np.transpose(ima)
    cv2.imwrite('make_cosines/2_saw.jpg', ima)


def make_texture(width, height, value):
    'background light'
    ima = np.full((width, height), value)
    ima = np.transpose(ima)
    cv2.imwrite('make_cosines/0_saw.jpg', ima)


# file = '/home/samir/PycharmProjects/db2/scan/static/scan_folder/gamma_im_folder/image1.png'
# gamma_correct = compensate_gamma(file)


make_texture(WIDTH, HEIGHT, 180)
make_triangle(WIDTH, HEIGHT, HFPERIODS)
make_sinusoidal(WIDTH, HEIGHT, HFPERIODS, 0)
