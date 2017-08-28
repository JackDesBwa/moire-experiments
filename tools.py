#!/usr/bin/env python3

import numpy as np
from PIL import Image
from PIL.ImageChops import multiply

def cos_shape(freq):
    return lambda x: 0.5+np.cos(2*np.pi*freq*x)/2

def bars_phase(angle_deg):
    a = np.sin(angle_deg/180*np.pi)
    return lambda x, y: x + a * y

def create_grating(size, shape, phase):
    npimg = np.indices((size[1],  size[0]), dtype='d')[1]
    for y in range(size[1]):
        npimg[y] = shape(phase(npimg[y], y))
    return Image.fromarray(np.uint8(npimg*255))

def merge_gratings(gratings):
    n = len(gratings)
    size = gratings[0].size
    img = Image.new('L', (size[0], (n+1)*size[1]+n*10), 255)
    moire = Image.new('L', size, 255)
    for i, g in enumerate(gratings):
        img.paste(g, (0, i*(size[1]+10)))
        moire = multiply(moire, g)
    img.paste(moire, (0, n*(size[1]+10)))
    return img
