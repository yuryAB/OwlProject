#https://www.pensador.com/frases/
from bs4 import BeautifulSoup
import requests

url = 'https://www.pensador.com/frases/'
site = requests.get(url)

soup = BeautifulSoup(site.text, 'html')

print(soup.prettify())

