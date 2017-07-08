from __future__ import division

import ppm
import cmath
from concurrent.futures import ProcessPoolExecutor, as_completed

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
sy = 5000
dx = 4
ox = -0.8


def process_column(x_coord):
    col = []
    x = x_coord
    for y in range(sy):
        px = (x - sx/2) * (dx/sx) + ox
        py = (y - sy/2) * (dx/sx)

        res = gen_point(complex(px, py))

        col.append(res)

    return col


def main():
    grid = []
    with ProcessPoolExecutor() as executor:
        try:
            futures = [executor.submit(process_column, x) for x in range(sx)]

            # Show the bar, wait for completion
            progress = tqdm(as_completed(futures),
                            total=len(futures),
                            unit='col',
                            leave=True)
            for _ in progress:
                pass
        except KeyboardInterrupt:
            for f in futures:
                f.cancel()

        # Append them to grid, in order
        for f in futures:
            grid.append(f.result())

        ppm.save_img('result.ppm', grid)


if __name__ == '__main__':
    main()

