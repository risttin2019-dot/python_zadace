# 1. zadatak

def cel_into_far(celsius):
    return celsius * 1.80 + 32

print(cel_into_far(32))

# output: 89.9


# 2. zadatak

def dan(broj):
    if broj is not None and (broj >= 1 and broj <= 7):
        if broj == 1:
            return 'Ponedjeljak'
        elif broj == 2:
            return 'Utorak'
        elif broj == 3:
            return 'Srijeda'
        elif broj == 4:
            return 'Četvrtak'
        elif broj == 5:
            return 'Petak'
        elif broj == 6:
            return 'Subota'
        elif broj == 7:
            return 'Nedjelja'
        
    return 'Pogrešan unos'

print(dan(0))
print(dan(None))
print(dan(5))

"""
output:
Pogrešan unos
Pogrešan unos
Petak
"""


# 3. zadatak

lista1 = [5, -3, 8, -6, 7, -2]
lista2 = [5, 9, 8, 6, 7, 2]

def najveci_negativni(lista):
    najveci = None

    for broj in lista:
        if broj < 0:
            if najveci is None or broj > najveci:
                najveci = broj

    return najveci

print(najveci_negativni(lista1))
print(najveci_negativni(lista2))

"""
output:
-2
None
"""

# 4. zadatak

lista = [2, 3, 4, 5, 6, 7, -2, -8, 11]

def broj_parnih(lista):
    parni = 0

    for broj in lista:
        if broj % 2 == 0:
            parni += 1

    return parni

print(broj_parnih(lista))

# output: 5


# DODATNI ZADACI


# 1. Zadatak

def suma_brojeva(lista):
    suma_dva = 0
    suma_tri = 0

    for broj in lista:
        if broj % 2 == 0:
            suma_dva += broj
        if broj % 3 == 0:
            suma_tri += broj

    return suma_dva, suma_tri


lista = [2, 4, 9, 6, 7]
print(suma_brojeva(lista))

# output: (12, 15)