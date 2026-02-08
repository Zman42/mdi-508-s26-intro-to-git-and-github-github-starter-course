import sys
import csv

filename = sys.argv[1]

with open(filename, "r") as f:
    reader = csv.reader(f)
    row = next(reader)
    numbers = [int(x) for x in row]
    print(int(sum(numbers)))
