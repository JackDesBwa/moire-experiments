#!/usr/bin/env python3

import sys
from tools import *

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
angles = np.random.random(msgsize)*np.pi
phases = np.random.random(msgsize)*2*np.pi

def phase(en):
    def ph(x, y):
        ym = y//pw
        x01 = (x % pw) / pw
        y01 = (y % pw) / pw
        a = angles[ym,:].repeat(pw)
        p = phases[ym,:].repeat(pw)
        m = msg[ym,:].repeat(pw)
        o = (x01*np.sin(a)+y01*np.cos(a))
        o += en*m/2/freq+p
        return o
    return ph

img1 = create_grating(imgsize, cos_shape(freq), phase(False))
img2 = create_grating(imgsize, cos_shape(freq), phase(True))

img = merge_gratings((img1, img2), True)
img.show()
