# csv_shape.py
import sys
import numpy as np

if __name__ == "__main__":
    fname = sys.argv[1]

    arr = np.genfromtxt(fname, delimiter=",")

    if arr.ndim == 0:
        rows, cols = 1, 1
    elif arr.ndim == 1:
        rows, cols = 1, arr.size
    else:
        rows, cols = arr.shape

    print(f"{rows} {cols}")
