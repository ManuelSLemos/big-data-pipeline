# Importamos dependencias
import requests # Consultar a paginas webs o apis 
import pandas # Organizar los datos
import json

# Crear el esqueleto de datos que extraemos del API
df = pandas.DataFrame([], columns=['id', 'name', 'status', 'species', 'kind', 'gender', 'origin', 'location'])

# Consultado una API
URL = "https://rickandmortyapi.com/api/character"
external_data = requests.get(URL).text # string

# String a JSON
external_json = json.loads(external_data)

for i in range(0, 20, 1):
    # Navegado por el JSON para extraer datos
    id = external_json['results'][i]['id']
    name = external_json['results'][i]['name']
    status = external_json['results'][i]['status']
    species = external_json['results'][i]['species']
    kind = external_json['results'][i]['type']
    gender = external_json['results'][i]['gender']
    origin = external_json['results'][i]['origin']['name']
    location = external_json['results'][i]['location']['name']

    # Agregar un nuevo registro utilizando _append()
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

df.to_csv('rick.csv', index=False)
