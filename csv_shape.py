import sys
import csv

filename = sys.argv[1]

with open(filename, "r") as f:
    reader = csv.reader(f)
    rows = list(reader)

num_rows = len(rows)
num_cols = len(rows[0]) if num_rows > 0 else 0

print(num_rows, num_cols)