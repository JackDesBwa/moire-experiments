#!/usr/bin/env python3

from tools import *

def phase(a):
    def ph(x, y):
        x -= 100
        y -= 100
        o = (x**2+y**2)/800
        np.clip(o, 0, 90**2/800, out=o)
        return o + a * (x+y)
    return ph

size = (200, 200)
img1 = create_grating(size, cos_shape(0.2), phase(-1))
img2 = create_grating(size, cos_shape(0.2), phase(+1))
img = merge_gratings((img1, img2))
np2pil(img).show()
