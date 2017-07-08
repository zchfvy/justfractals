from __future__ import division

import ppm
import cmath

from tqdm import tqdm

def gen_point(c, iters=50):
    z = complex(0, 0)
    try:
        for i in range(iters):
            z = z**2 + c
            if abs(z) > 8.0:
                return i/iters
        return 0
    except OverflowError:
        return i/iters


sx = 10000
sy = 6000
dx = 4
ox = -0.8

grid = [[0 for x in range(sx)] for y in range(sy)]

for x in tqdm(range(sx)):
    for y in tqdm(range(sy)):
        px = (x - sx/2) * (dx/sx) + ox
        py = (y - sy/2) * (dx/sx)

        res = gen_point(complex(px, py))

        grid[y][x] = res

ppm.save_img('result.ppm', grid)

