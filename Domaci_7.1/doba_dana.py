# 1. zadatak

hour = 0
daytime = None

while hour < 24:
    if hour >= 6 and hour < 12:
        print(f'Vrijeme: {hour}h, doba dana: jutro')
        hour += 1
    elif hour >= 12 and hour < 18:
        print(f'Vrijeme: {hour}h, doba dana: popodne')
        hour += 1
    elif hour >= 18 and hour < 22:
        print(f'Vrijeme: {hour}h, doba dana: veče')
        hour += 1
    else:
        print(f'Vrijeme: {hour}h, doba dana: noć')
        hour += 1