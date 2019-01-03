#!/usr/bin/env python3

from tools import *

size = (50, 800)
img1 = create_grating(size, cos_shape(0.10), bars_phase(-2))
img2 = create_grating(size, cos_shape(0.12), bars_phase(2))
img = merge_gratings((img1, img2), True)
img.show()
