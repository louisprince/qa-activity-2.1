#!/bin/python3

file = open("./car_sale.csv")
lines = file.readlines()
headers = str(lines[0]).replace('\n', '').split(',')
companies: list[dict[str, str]] = list()

for line in range(1, len(lines), 1):
    company: dict[str, str] = {}
    columns = str(lines[line]).replace('\n', '').split(',')
    for column in range(0, len(columns), 1):
        key = headers[column]
        company[key] = columns[column]
    companies.append(company)

grand_total = 0

for column in range(1, len(headers), 1):
    month = headers[column]
    total = 0
    for company in companies:
        total += int(company[month])
    print(f"Total cars sold in {month} is {total}")
    grand_total += total

print(f"The grand total of cars sold is {grand_total}\n")

for company in companies:
    name = company["Company"]
    total = 0
    for column in range(1, len(headers), 1):
        month = headers[column]
        total += int(company[month])
    print(f"Total for {name} is {total}")
