#!/usr/bin/env python3

from moire_utils import *

def phaser(en):
    def ph(x, y):
        x -= 0.5
        y -= 0.5
        w = x**2+y**2
        e = (w > 0.0178) * (w < 0.25)
        o = (np.arctan2(x, y)/np.pi+1)/2
        p = 1
        p *= ((x-1/3)**2+y**2)*5
        p *= ((x+1/3)**2+y**2)*5
        p *= (x**2+(y-1/3)**2)*5
        p *= (x**2+(y+1/3)**2)*5

        return o*e, p*e*en
    return ph

size = (300, 300)
img1 = grating(size, 80, wave_cos(), phaser(-1))
img2 = grating(size, 80, wave_cos(), phaser(1))
imshow((img1, img2, img1*img2))
