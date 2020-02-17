import csv

with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["loyer"], row["surface"])