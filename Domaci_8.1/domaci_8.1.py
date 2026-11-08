# 1. zadatak

def get_even_positions(data):
    even_num_index = []

    for i in range(0, len(data), 2):
        even_num_index.append(data[i])

    return tuple(even_num_index)

tuple1 = (10, 20, 30, 40, 50, 60)
print(get_even_positions(tuple1))


# 2. zadatak

def find_exclusive_students(group1, group2):
    return group1 - group2

set1 = {'Ana', 'Marko', 'Jovan', 'Milica'}
set2 = {'Marko', 'Milica' ,'Petar'}

print(find_exclusive_students(set1, set2))

#

# 3. zadatak

def clean_tags(text):
    trimmed = text.strip()
    lowered = trimmed.lower()
    seperated = lowered.split(' | ')
    cleaned = '-'.join(seperated)

    return cleaned

text1 = ' Python | DATA | SQL '
print(clean_tags(text1))


# 4. zadatak

csv_file = [
    'customer,product,quantity',
    'Alice,laptop,2',
    'Bob,mouse,3',
    'Alice,laptop,1',
    'Charlie,keyboard,2',
    'Bob,mouse,1'
]

def count_products(csv_lines):
    sold = {}

    for line in csv_lines[1:]:
        parts = line.split(',')

        product = parts[1]
        quantity = int(parts[2])

        sold[product] = sold.get(product, 0) + quantity

    return sold

print(count_products(csv_file))