#!/usr/bin/env python3

from tools import *

def phase(a):
    def ph(x, y):
        h = 150
        x -= h
        y -= h
        o = (np.arctan2(x, y)/np.pi+1)/2*np.pi
        q = 100
        oo = a/10
        oo *= ((x-q)**2+y**2)/h**2
        oo *= ((x+q)**2+y**2)/h**2
        oo *= (x**2+(y-q)**2)/h**2
        oo *= (x**2+(y+q)**2)/h**2
        o += oo
        j = x**2+y**2 > 40**2
        k = x**2+y**2 < h**2
        return j*o*k
    return ph

size = (300, 300)
img1 = create_grating(size, cos_shape(80/np.pi), phase(-1))
img2 = create_grating(size, cos_shape(80/np.pi), phase(+1))
img = merge_gratings((img1, img2))
img.show()
