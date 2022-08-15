#!/usr/bin/env python3

from moire_utils import *

def phaser(en):
    def ph(x, y):
        x -= 0.5
        y -= 0.5
        o = (x + y) / 2
        p = np.clip(10*(x**2+y**2), 0, 10*(0.45**2))
        return o, en*p
    return ph

size = (200, 200)
img1 = grating(size, 80, wave_cos(), phaser(-1))
img2 = grating(size, 80, wave_cos(), phaser(1))
imshow((img1, img2, img1*img2))
