#!/usr/bin/env python3

import sys
from tools import *

def phase(f, b, a):
    def ph(x, y):
        o = (x+1.4*y)/300
        o += a * np.arccos((f[y]/255.0*2)-1)/250
        if b is not None:
            o += (np.arccos((b[y]/255.0*2)-1))/80
        return o
    return ph

f_file = '5_pattern.png'
if len(sys.argv) > 1:
    f_file = sys.argv[1]

image = Image.open(f_file);
size = (image.size[1], image.size[0])

f = np.array(tuple(i[0] for i in image.getdata()), dtype=np.uint8).reshape(size)

b = None
if len(sys.argv) > 2:
    b = np.array(tuple(i[0] for i in Image.open(sys.argv[2]).getdata()), dtype=np.uint8).reshape(size)

img1 = create_grating(size, cos_shape(20), phase(f, b, -1))
img2 = create_grating(size, cos_shape(20), phase(f, b, +1))

img = merge_gratings((img1, img2))
img.show()
