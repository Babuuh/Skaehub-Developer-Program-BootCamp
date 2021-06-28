import csv

file = csv.DictReader(open('Day 1/addresses.csv'))

for row in file:
    print(row)