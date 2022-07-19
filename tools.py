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
    npimg = np.indices((size[0],  size[1]), dtype='d')[1]
    for y in range(size[0]):
        npimg[y] = shape(phase(npimg[y], y))
    return Image.fromarray(np.uint8(npimg*255))

def merge_gratings(gratings, vert=False):
    if vert:
        n = len(gratings)
        size = gratings[0].size
        img = Image.new('L', (size[0], (n+1)*size[1]+n*10), 255)
        moire = Image.new('L', size, 255)
        for i, g in enumerate(gratings):
            img.paste(g, (0, i*(size[1]+10)))
            moire = multiply(moire, g)
        img.paste(moire, (0, n*(size[1]+10)))
    else:
        n = len(gratings)
        size = gratings[0].size
        img = Image.new('L', ((n+1)*size[0]+n*10, size[1]), 255)
        moire = Image.new('L', size, 255)
        for i, g in enumerate(gratings):
            img.paste(g, (i*(size[0]+10), 0))
            moire = multiply(moire, g)
        img.paste(moire, (n*(size[0]+10), 0))
    return img

def hexgrid(size, f):
    img = np.indices(size, dtype='d')[1]/size[1]
    res = np.zeros((*size, 3))

    for yi in range(img.shape[0]):
        x = img[yi,:]
        y = yi/size[1] # In same scale as x

        sz = np.sqrt(3)/f/3
        qf = (np.sqrt(3)/3 * x  -  1/3 * y) / sz
        rf = y * 2/3 / sz
        sf = -qf-rf

        q = np.round(qf)
        r = np.round(rf)
        s = np.round(sf)

        qd = np.abs(q - qf)
        rd = np.abs(r - rf)
        sd = np.abs(s - sf)

        qm = (qd > rd) * (qd > sd)
        q = q * (1 - qm) + (-r-s) * qm
        rm = (1 - qm) * (rd > sd)
        r = r * (1 - rm) + (-q-s) * rm
        sm = (1 - rm)
        s = s * (1 - sm) + (-q-r) * sm

        res[yi, :, 0] = q
        res[yi, :, 1] = r
        res[yi, :, 2] = s

    return res

def trihexgrid(size, f):
    hexs = hexgrid(size, f)
    return (hexs[:,:,0]-hexs[:,:,1])%3

def quadhexgrid(size, f):
    hexs = hexgrid(size, f)
    return (hexs[:,:,0]+hexs[:,:,1]*2)%4
