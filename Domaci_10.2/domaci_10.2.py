import numpy as np

# 1. zadatak

aktivni_korisnici = np.array([120, 150, 180, 210, 340, 290, 310, 420, 390, 280, 190, 140])

prvih_pet_sati = aktivni_korisnici[4]
print(prvih_pet_sati)

posljednjih_4_sata = aktivni_korisnici[-4:]
print(posljednjih_4_sata)

ukupan_broj_korisnika = aktivni_korisnici.sum()
print(ukupan_broj_korisnika)

najaktivniji_sat = aktivni_korisnici.max()
print(najaktivniji_sat)


# 2. zadatak

server1 = [45, 85, 81]
server2 = [35, 31, 77]
server3 = [30, 25, 70]
server4 = [52, 35, 62]
server5 = [55, 82, 41]

sistem = np.array([server1, server2, server3, server4, server5])
print(sistem.shape)

broj_servera, broj_metrika = sistem.shape
print(f'Broj servera: {broj_servera}, broj metrika: {broj_metrika}')

prosek_metrika = np.mean(sistem, axis=0)
print('Prosjek svake metrike (CPU, RAM, Disk):', prosek_metrika)

prosek_servera = np.mean(sistem, axis=1)
print('Prosjek po serverima:',prosek_servera)

najoptereceniji_server = np.argmax(prosek_servera) + 1
print('Server sa najvećom prosečnom potrošnjom:', najoptereceniji_server)


# 3. zadatak

procesi = np.array([25, 110, 45, 80, 150, 30, 95, 60, 120, 40, 15, 105, 70, 50, 130])

duze_od_100_sekundi = procesi[procesi > 100]
print(duze_od_100_sekundi)

izmedju_40_i_100 = procesi[(procesi >= 40) & (procesi <= 100)]
print(izmedju_40_i_100)

broj_kracih_od_50_sek = len(procesi[procesi < 50])
print(broj_kracih_od_50_sek)

indeksi = np.where(procesi > 100)[0]
print(indeksi)

ukupno_vrijeme_izvrsavanja = procesi.mean()
print(ukupno_vrijeme_izvrsavanja)


# 4. zadatak

kategorija1 = [1200, 1500, 1400, 1600, 1800, 2000]
kategorija2 = [800, 950, 1100, 1050, 1200, 1300]
kategorija3 = [2500, 2400, 2600, 2700, 3000, 3200]
kategorija4 = [600, 700, 650, 750, 800, 900]

prihodi = np.array([kategorija1, kategorija2, kategorija3, kategorija4])

print(prihodi)

prihod_po_kategoriji = np.sum(prihodi, axis=1)
print(prihod_po_kategoriji)

prihod_po_mjesecu = np.sum(prihodi, axis=0)
print(prihod_po_mjesecu)

najveci_prihod_po_kategoriji = np.where(prihod_po_kategoriji == prihod_po_kategoriji.max())[0][0]
print(najveci_prihod_po_kategoriji)

najveci_prihod_po_mjesecu = np.where(prihod_po_mjesecu == prihod_po_mjesecu.max())[0][0]
print(najveci_prihod_po_mjesecu)

prosjek_po_kategoriji = np.mean(prihodi, axis=1)
print(prosjek_po_kategoriji)

prosjek_po_mjesecu = np.mean(prihodi, axis=0)
print(prosjek_po_mjesecu)


# 5. zadatak

temperature = np.array([22.5, 18.0, -25.4, 15.2, None, 30.1, 55.8, 21.0, 19.4, 12.4, None, -22.1, 28.5, 60.0, 17.6], dtype=object)

print(temperature)

for i, value in enumerate(temperature):
    if value is None:
        print(f'Vrijednost je: {value}')

for i, value in enumerate(temperature):
    if value is not None:
        if value <= -20 or value >= 50:
            print(f'Temperature nije u validnom opsegu: {value}')

for i, value in enumerate(temperature):
    if value is not None:
        if value <= -20 or value >= 50:
            print(f'Temperature nije u validnom opsegu na indeksu: {i}')
    else:
        print(f'Element nema vrijednost na indeksu: {i}')

counter = 0

for i, value in enumerate(temperature):
    if value is not None:
        if value <= -20 or value >= 50:
            counter += 1
    else:
        counter += 1
    

print(f'Broj nevalidnih i nedostajućih vrijednosti: {counter}')

procenat_neispravnih = counter * 100 / len(temperature) 
print(f'Procenat neispravnih: {procenat_neispravnih}%')

validne_temperature = []

for i, value in enumerate(temperature):
    if value is not None:
        if value >= -20 and value <= 50:
            validne_temperature.append(value)

print(validne_temperature)

print(np.mean(validne_temperature))