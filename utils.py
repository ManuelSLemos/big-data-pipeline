import requests 
import json

from constants import CHARACTER_URL_BASE

page_source = requests.get(CHARACTER_URL_BASE).text
data_json = json.loads(page_source)

total_pages = data_json['info']['pages']
character_count = len(data_json['results'])