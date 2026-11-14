# 1. zadatak

def safe_divide(a, b):
    try:
        return float(a / b)
    except (ZeroDivisionError, ValueError, TypeError):
        return None

print(safe_divide(10, 2))
print(safe_divide(10, 'sda'))


# 2. zadatak

def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None
    
print(safe_int('25'))
print(safe_int('-10'))
print(safe_int('abc'))


# 3. zadatak

def get_grade(grades, student):
    try:
        return grades[student]
    except KeyError:
        return None

print(get_grade({'Ana': 5, 'Marko': 4, 'Jovana': 5}, 'Marko'))
print(get_grade({'Ana': 5, 'Marko': 4, 'Jovana': 5}, 'Petar'))


# 4. zadatak

def read_file(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return 'File not found'
        
print(read_file('data/raw/teams22.csv'))


# 5. zadatak

def sum_numbers(values):
    total = 0
    for v in values:
        try:
            total += float(v)
        except (ValueError, TypeError):
            pass
    return total

print(sum_numbers(['10', '5.5', 'abc', '3', 'hello']))


# 6. zadatak

def get_age(csv_line):
    try:
        return int(csv_line.split(',')[1])
    except:
        return None

print(get_age('Ana,22'))
print(get_age('Marko,abc'))
print(get_age('Jovana'))