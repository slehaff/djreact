"This module does bla bla"
import math
import cv2
import numpy as np


WIDTH = 1920
height = 1080
periods = 1
HFPeriods = 100


def makeTRiangle(width, height, hfPeriods):
    "This functtion makes a sawtooth wave"
    ima = np.zeros((width, height))
    imaline = np.ones(width)
    raw_inp = np.ones(width)
    for i in range(width):
        raw_inp[i] = 255.0*(hfPeriods * i/width -
                            math.trunc(hfPeriods * i/width))
        imaline[i] = raw_inp[i]
    for j in range(height):
        ima[:, j] = imaline
    ima = np.transpose(ima)
    cv2.imwrite('cosines/1_saw.jpg', ima)


def maketexture(w, h, value):
    'text'
    ima = np.full((w, h), value)
    ima = np.transpose(ima)
    cv2.imwrite('cosines/0_saw.jpg', ima)

# file = '/home/samir/PycharmProjects/db2/scan/static/scan_folder/gamma_im_folder/image1.png'
# gamma_correct = compensate_gamma(file)


maketexture(WIDTH, height, 100)
makeTRiangle(WIDTH, height, HFPeriods)
