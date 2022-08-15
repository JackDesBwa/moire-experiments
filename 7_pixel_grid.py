#!/usr/bin/env python3

import sys
from moire_utils import *

f_msg = '7_msg.pbm'
if len(sys.argv) > 1:
    f_msg = sys.argv[1]

freq = 5
pw = 25
msg = Image.open(f_msg).convert('L');
msgsize = (msg.size[1], msg.size[0])
imgsize = (msg.size[1]*pw, msg.size[0]*pw)

np.random.seed(0)
msg = np.array(msg.getdata(), dtype=np.uint8).reshape(msgsize)/255
msg = msg.repeat(pw, axis=0).repeat(pw, axis=1)
angles = np.random.random(msgsize)*np.pi
angles = angles.repeat(pw, axis=0).repeat(pw, axis=1)
phases = np.random.random(msgsize)*2*np.pi
phases = phases.repeat(pw, axis=0).repeat(pw, axis=1)

def phaser(size, en):
    def ph(x, y):
        xs = (x % (pw/size[1])) * size[1]/ pw
        ys = (y % (pw/size[0])) * size[0]/ pw
        p = phases + en * msg * 0.5
        o = xs * np.sin(angles) + ys * np.cos(angles)
        return o, p
    return ph

img1 = grating(imgsize, freq, wave_cos(), phaser(imgsize, False))
img2 = grating(imgsize, freq, wave_cos(), phaser(imgsize, True))
imshow((img1, img2, img1*img2), True)
