#!/usr/bin/env python3

from moire_utils import *

def phaser(en):
    def ph(x, y):
        x -= 0.5
        y -= 0.5
        w = x**2+y**2
        e = (w > 0.0178) * (w < 0.25)
        ag = np.arctan2(x, y)
        r = (np.sqrt(w)-0.13)/(0.5-0.13)
        o = (np.arctan2(x, y)/np.pi+1)/2
        p = np.mod(r-ag/6, np.pi/3)*3/np.pi
        return o*e, p*e*en
    return ph

size = (300, 300)
img1 = grating(size, 80, wave_cos(), phaser(-1))
img2 = grating(size, 80, wave_cos(), phaser(1))
imshow((img1, img2, img1*img2))
