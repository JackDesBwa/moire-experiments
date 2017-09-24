#!/usr/bin/env python3

import sys
from tools import *

def phase(f, a):
    def ph(x, y):
        o = (x+1.4*y)/300
        o += a * (np.arccos((f[y]/255.0*2)-1)/np.pi+1)/2/200
        return o
    return ph

size = (300, 300)

img = [0,0,0]
f_file = '6_pattern.png'
if len(sys.argv) > 1:
    f_file = sys.argv[1]
for chan in range(3):
    f = np.array(tuple(i[chan] for i in Image.open(f_file).getdata()), dtype=np.uint8).reshape(size)

    img1 = create_grating(size, cos_shape(90), phase(f, +0.5))
    img2 = create_grating(size, cos_shape(90), phase(f, -0.5))

    img[chan] = merge_gratings((img1, img2))

img = Image.merge('RGB', (img[0], img[1], img[2]))
img.show()
