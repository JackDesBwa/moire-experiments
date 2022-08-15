#!/usr/bin/env python3

import sys
from moire_utils import *

def phaser(f, a, en):
    s = np.sin(a/180*np.pi)
    c = np.cos(a/180*np.pi)
    def ph(x, y):
        o = c*x+s*y
        p = en/2 * np.arccos(2*f-1)/(2*np.pi)
        return o, p
    return ph

f_file = '6_pattern.png'
if len(sys.argv) > 1:
    f_file = sys.argv[1]

image = np.array(Image.open(f_file), dtype=np.double)/255
size = image.shape[:2]
fq = 80

img1 = np.stack([
    grating(size, fq, wave_cos(), phaser(image[...,chan], 60, -1)) for chan in range(3)
], axis=2)

img2 = np.stack([
    grating(size, fq, wave_cos(), phaser(image[...,chan], 60, +1)) for chan in range(3)
], axis=2)

imshow((img1, img2, img1*img2))
