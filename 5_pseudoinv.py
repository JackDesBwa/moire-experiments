#!/usr/bin/env python3

import sys
from moire_utils import *

def phaser(f, b, a, en):
    s = np.sin(a/180*np.pi)
    c = np.cos(a/180*np.pi)
    def ph(x, y):
        o = c*x+s*y
        p = en/2 * np.arccos(2*f-1)/(2*np.pi)
        p += 0 if b is None else 2*((np.arccos(2*b-1))/(2*np.pi))
        return o, p
    return ph

f_file = '5_pattern.png'
if len(sys.argv) > 1:
    f_file = sys.argv[1]

f = np.array(Image.open(f_file).convert('L'), dtype=np.double)/255
b = np.array(Image.open(sys.argv[2]).convert('L'), dtype=np.double)/255 if len(sys.argv) > 2 else None
size = f.shape

img1 = grating(size, 60, wave_cos(), phaser(f, b, 45, -1))
img2 = grating(size, 60, wave_cos(), phaser(f, b, 45, +1))

imshow((img1, img2, img1*img2))
