#!/usr/bin/env python3

import sys
from tools import *

f_files = ['8_1.png', '8_2.png', '8_3.png']
if len(sys.argv) > 3:
    f_files = sys.argv[1:4]

fs = list(map(lambda x: np.array(Image.open(x).convert('L'), dtype=np.double)*2/255-1, f_files))
size = fs[0].shape
angles = [10, 65, 120]
fq = 100

for f in fs:
    if not f.shape == size:
        print('Image sizes do not match')
        exit(1)

def phase(f, a, en):
    s = np.sin(a/180*np.pi)
    c = np.cos(a/180*np.pi)
    def ph(xi, yi):
        x = xi/size[1]
        y = yi/size[0]
        o = c*x+s*y
        o += en * np.arccos(f[yi])/2/fq/np.pi
        return o
    return ph

thg = trihexgrid(size, fq/2)
img = np.zeros(size, dtype=np.double)
for i, f in enumerate(fs):
    img += create_grating(size, cos_shape(fq), phase(f, angles[i], 1))*(thg==i)

allimgs = []
for i in range(3):
    img2 = create_grating(size, cos_shape(fq), phase(f, angles[i], 0))
    allimgs.append(merge_gratings((img, img2)))
    allimgs.append(np.ones((10, size[1]*3+20)))

res = np.concatenate(allimgs, axis=0)
res[0:size[0], 0:size[1]] = 1
res[size[0]*2+20:, 0:size[1]] = 1

imshow(res)
