#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def imshow(imgs, vertical=False, cmap='gray'):
    if type(imgs) is np.ndarray: imgs = (imgs, )
    if vertical is False: vertical = (1, len(imgs))
    if vertical is True: vertical = (len(imgs), 1)
    if len(imgs) == 0: return

    ax1 = None
    for i, img in enumerate(imgs, 1):
        if not img is None:
            if ax1 is None:
                ax1 = ax2 = plt.subplot(vertical[0], vertical[1], i)
            else:
                ax2 = plt.subplot(vertical[0], vertical[1], i, sharex=ax1, sharey=ax1)
            ax2.imshow(img, cmap=cmap)
    plt.tight_layout()
    plt.show()

def gen_uv(size):
    y, x = np.indices(size, dtype=np.double)
    y /= size[0]
    x /= size[1]
    return x, y

def wave_cos():
    return lambda x: 0.5 + np.cos(2*np.pi*x)/2

def phaser_linear(angle_deg, ratio=1):
    angle_rad = np.arctan(np.tan(angle_deg * np.pi / 180) / ratio)
    s = np.sin(angle_rad)
    c = np.cos(angle_rad)
    return lambda x, y: (c * x + s * y, 0)

def grating(size, freq, wave, phaser):
    x, y = gen_uv(size)
    o, p = phaser(x, y)
    return wave((freq*o+p)%1)

def merge(gratings, vert=False, add_moire=True):
    imgs = []
    spacer = np.ones((10 if vert else gratings[0].shape[0], gratings[0].shape[1] if vert else 10))
    if len(gratings[0].shape) == 3: spacer = np.stack((spacer, spacer, spacer), axis=2)
    moire = np.ones(gratings[0].shape, dtype=np.double)
    for g in gratings:
        moire *= g
        imgs.append(g)
        imgs.append(spacer)
    if add_moire:
        imgs.append(moire)

    ax = 0 if vert else 1
    return np.concatenate(imgs, axis=ax)

def np2pil(img):
    return Image.fromarray(np.uint8(img*255))

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
