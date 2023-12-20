import requests 
import pandas
import json

from constants import CHARACTER_URL_WITH_PAGINATION

from utils import (
    total_pages,
    character_count
)

df = pandas.DataFrame([], columns=['id', 'name', 'status', 'species', 'kind', 'gender', 'origin', 'location'])

for page in range(1, total_pages + 1, 1):
    URL = f'{CHARACTER_URL_WITH_PAGINATION}{page}'

    page_source = requests.get(URL).text
    to_json = json.loads(page_source)

    try:
        for i in range(0, character_count, 1):
            id = to_json['results'][i]['id']
            name = to_json['results'][i]['name']
            status = to_json['results'][i]['status']
            species = to_json['results'][i]['species']
            kind = to_json['results'][i]['type']
            gender = to_json['results'][i]['gender']
            origin = to_json['results'][i]['origin']['name']
            location = to_json['results'][i]['location']['name']

            df = df._append({ 
                'id': id, 
                'name': name, 
                'status': status, 
                'species': species, 
                'kind': kind, 
                'gender': gender, 
                'origin': origin, 
                'location': location 
            }, ignore_index=True)
    except:
        print('Upps...')


df.to_csv('rick.csv', index=False)