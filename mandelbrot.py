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
                return False
        return True
    except OverflowError:
        return False


sx = 8000
sy = 4080
dx = 4
ox = -0.8

grid = [[0 for x in range(sx)] for y in range(sy)]

for x in tqdm(range(sx)):
    for y in tqdm(range(sy)):
        px = (x - sx/2) * (dx/sx) + ox
        py = (y - sy/2) * (dx/sx)

        res = gen_point(complex(px, py))

        if res:
            grid[y][x] = 1

ppm.save_img('result.ppm', grid)

