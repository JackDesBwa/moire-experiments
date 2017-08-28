#!/usr/bin/env python3

from PIL import Image
from PIL.ImageChops import multiply
from math import cos

def compute1(x, y):
    return int((0.5+cos((x-0.05*y)/2)/2)*255)

def compute2(x, y):
    return int((0.5+cos((x+0.05*y)/1.8)/2)*255)

size = (800, 50)
img1 = Image.new('L', size)
for x in range(img1.size[0]):
    for y in range(img1.size[1]):
        img1.putpixel((x, y), (compute1(x, y),))
img2 = Image.new('L', size)
for x in range(img2.size[0]):
    for y in range(img2.size[1]):
        img2.putpixel((x, y), (compute2(x, y),))
img = Image.new('L', (size[0], 3*size[1]+20), 255)
img.paste(img1, (0, 0))
img.paste(img2, (0, size[1]+10))
img.paste(multiply(img1, img2), (0, 2*size[1]+20))
img.show()
