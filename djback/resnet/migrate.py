"This module does bla bla"
import cv2
import numpy as np
from PIL import Image
import math


WIDTH = 854
height = 480
periods = 1
hfPeriods = 10


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
    cv2.imwrite('tri.jpg', ima)


def makeimage(w, h, wvcount, phi):
    "This function does bla bla"
    ima = np.zeros((w, h))
    imaline = np.ones(w)
    raw_inp = np.ones(w)
    for i in range(w):
        raw_inp[i] = 255.0*(1.0/2.0 + 1.0/2.0*np.cos(2.0*np.pi *
                                                     (1.0*float(phi)/3.0 + wvcount*float(i)/float(w))))
        # imaline[i] = np.polyval(gamma_correct, raw_inp[i])
        imaline[i] = raw_inp[i]
    for j in range(h):
        ima[:, j] = imaline
    ima = np.transpose(ima)
    cv2.imwrite(str(phi + 1) + '_cos.jpg', ima)


def maketexture(w, h, value):
    ima = np.full((w, h), value)
    ima = np.transpose(ima)
    cv2.imwrite('texture.png', ima)

# file = '/home/samir/PycharmProjects/db2/scan/static/scan_folder/gamma_im_folder/image1.png'
# gamma_correct = compensate_gamma(file)


makeimage(WIDTH, height, hfPeriods, -1)
makeimage(WIDTH, height, hfPeriods, 0)
makeimage(WIDTH, height, hfPeriods, 1)
makeimage(WIDTH, height, periods, 5)
makeimage(WIDTH, height, periods, 6)
makeimage(WIDTH, height, periods, 7)
maketexture(WIDTH, height, 100)
makeTRiangle(WIDTH, height, hfPeriods)
