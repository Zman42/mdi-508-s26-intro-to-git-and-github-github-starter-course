import sys
import csv

number_sum.csv = sys.argv[1]

with open(number_sum.csv, "r") as f:
    reader = csv.reader(f)
    row = next(reader)
    numbers = [int(x) for x in row]
    print(int(sum(numbers)))
