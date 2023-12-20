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

# Navegado por el JSON para extraer datos
id = external_json['results'][0]['id']
name = external_json['results'][0]['name']
status = external_json['results'][0]['status']
species = external_json['results'][0]['species']
kind = external_json['results'][0]['type']
gender = external_json['results'][0]['gender']
origin = external_json['results'][0]['origin']['name']
location = external_json['results'][0]['location']['name']

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

# df.to_csv('rick.csv', index=False)