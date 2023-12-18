
import requests
# import selenium
from bs4 import BeautifulSoup

URL = 'https://rick-and-morty-gui-leandro.vercel.app/'

source_page = requests.get(URL).text
soup = BeautifulSoup(source_page, 'html.parser')

elements = soup.select('.home__CharContainer-sc-14ot2xn-4')

for element in elements:
    name = element.select_one('span').text.split(' ')[0]
    last_name = element.select_one('span').text.split(' ')[1]
    image = element.select_one('img')['src']
    
    print(last_name, image)
    print(f'INSERT INTO Estudiantes ( nombre, apellidos, foto) VALUES ({name}, {last_name}, {image})')