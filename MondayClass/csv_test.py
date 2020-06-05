import csv
with open('tieba.csv',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)