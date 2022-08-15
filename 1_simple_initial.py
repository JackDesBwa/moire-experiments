#!/usr/bin/env python3

from moire_utils import *

size = (50, 800)
ratio = size[1]/size[0]
img1 = grating(size, 80, wave_cos(), phaser_linear(-2, ratio))
img2 = grating(size, 96, wave_cos(), phaser_linear(2, ratio))
imshow((img1, img2, img1*img2), True)
