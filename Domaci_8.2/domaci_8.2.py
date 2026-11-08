# 1. zadatak

import csv

def get_header(path):
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        
    return header

path_string = 'data/raw/teams.csv'

get_header(path_string)


# 2. zadatak

def read_rows(path):
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        rows = list(reader)
        
    return rows

path_string = 'data/raw/teams.csv'

read_rows(path_string)


# 3. zadatak

def total_points(path):
    total = 0

    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            total += int(row['points'])
            
    return total

path_string = 'data/raw/teams.csv'

total_points(path_string)


# 4. zadatak

def write_rows(path, rows):
    with open(path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

lista = [
    ['name', 'age'], 
    ['Ana', 20], 
    ['Marko', 22]
]

path_string = 'data/processed/people.csv'

write_rows(path_string, lista)


# 5. zadatak

def write_dicts(path, rows):
    with open(path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

list_dicts = [
    {'name': 'Ana', 'age': 20}, 
    {'name': 'Marko', 'age': 22}
]

path_string = 'data/processed/people.csv'

write_dicts(path_string, list_dicts)