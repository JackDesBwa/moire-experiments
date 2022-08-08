#!/usr/bin/env python3

from tools import *

def phase(a):
    def ph(x, y):
        h = 150
        x -= h
        y -= h
        ag = np.arctan2(x, y)
        r = (np.sqrt(x**2+y**2)-40)/(h-40)
        o = (np.arctan2(x, y)/np.pi+1)/2
        o -= a*np.mod(r-ag/6, np.pi/3)*3/np.pi/80
        j = x**2+y**2 > 40**2
        k = x**2+y**2 < h**2
        return j*o*k
    return ph

size = (300, 300)
img1 = create_grating(size, cos_shape(80), phase(-1))
img2 = create_grating(size, cos_shape(80), phase(+1))
img = merge_gratings((img1, img2))
imshow(img)
