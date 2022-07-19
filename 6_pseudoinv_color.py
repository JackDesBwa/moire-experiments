#!/usr/bin/env python3

import sys
from tools import *

def phase(f, a):
    def ph(x, y):
        o = (x+1.4*y)/300
        o += a * (np.arccos((f[y]/255.0*2)-1)/np.pi+1)/2/200
        return o
    return ph

f_file = '6_pattern.png'
if len(sys.argv) > 1:
    f_file = sys.argv[1]

image = Image.open(f_file);
size = (image.size[1], image.size[0])

img = [0,0,0]
for chan in range(3):
    f = np.array(tuple(i[chan] for i in image.getdata()), dtype=np.uint8).reshape(size)

    img1 = create_grating(size, cos_shape(90), phase(f, +0.5))
    img2 = create_grating(size, cos_shape(90), phase(f, -0.5))

    img[chan] = merge_gratings((img1, img2))

img = np.stack(img, axis=2)
np2pil(img).show()
