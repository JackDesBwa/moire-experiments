#!/usr/bin/env python3

import sys
from moire_utils import *

f_files = ['8_1.png', '8_2.png', '8_3.png']
if len(sys.argv) > 3:
    f_files = sys.argv[1:4]

fs = list(map(lambda x: np.array(Image.open(x).convert('L'), dtype=np.double)*2/255-1, f_files))
size = fs[0].shape
angles = [10, 65, 120]
fq = 100

for f in fs:
    if not f.shape == size:
        print('Image sizes do not match')
        exit(1)

def phaser(f, a, en):
    s = np.sin(a/180*np.pi)
    c = np.cos(a/180*np.pi)
    def ph(x, y):
        o = c*x+s*y
        p = en * np.arccos(f)/np.pi/2
        return o, p
    return ph

thg = trihexgrid(size, fq/2)
img1 = np.sum([grating(size, fq, wave_cos(), phaser(fs[i], a, 1))*(thg==i) for i, a in enumerate(angles)], axis=0)
revealers = [grating(size, fq, wave_cos(), phaser(f, a, 0)) for a in angles]

imshow((
    None, revealers[0], revealers[0]*img1,
    img1, revealers[1], revealers[1]*img1,
    None, revealers[2], revealers[2]*img1,
), (3, 3))
