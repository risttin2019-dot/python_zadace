import requests

# 1. zadatak

def get_space_station():
    url = 'http://api.open-notify.org/iss-now.json'
    r = requests.get(url)
    r.raise_for_status()

    data = r.json()

    return {
        'latitude': data['iss_position']['latitude'],
        'longitude': data['iss_position']['longitude']
    }

print(get_space_station()) 


# 2. zadatak

def get_universities(country):
    url = 'http://universities.hipolabs.com/search'
    params = {'country': country}

    r = requests.get(url, params=params)
    r.raise_for_status()

    data = r.json()

    return [uni['name'] for uni in data]

print(get_universities('Serbia'))


# 3. zadatak

def get_exchange_rate(base, target):
  url = 'https://api.frankfurter.dev/v1/latest'
  params = {'base': base, 'symbols': target}

  r = requests.get(url, params=params)
  r.raise_for_status()

  data = r.json()

  return data['rates'][target]

print(get_exchange_rate('EUR', 'USD'))

