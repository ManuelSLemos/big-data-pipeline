# Importamos dependencias
import requests # Consultar a paginas webs o apis 
import pandas # Organizar los datos
import json

# Crear el esqueleto de datos que extraemos del API
df = pandas.DataFrame([], columns=['id', 'name', 'status', 'species', 'type', 'gender', 'origin', 'location'])

URL = "https://rickandmortyapi.com/api/character"

external_data = requests.get(URL).text # string

external_json = json.loads(external_data)

print(external_json['results'][0]['name'])

id = external_json['results'][0]['id']
name = external_json['results'][0]['name']
status = external_json['results'][0]['status']
species = external_json['results'][0]['species']
kind = external_json['results'][0]['type']
gender = external_json['results'][0]['gender']
origin = external_json['results'][0]['origin']['name']
location = external_json['results'][0]['location']['name']

print(id, name, status, species, kind, gender, origin, location)