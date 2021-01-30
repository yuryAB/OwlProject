#https://www.pensador.com/frases/
from bs4 import BeautifulSoup
import requests

class PensadorCrawler: 
    def __init__(self):
        self.url = 'https://www.pensador.com/frases/'

    def getPhrasesFromUrl(self,url):
        site = requests.get(url)
        soup = BeautifulSoup(site.text, 'html')
        frase_fr_class = soup.findAll("p", {"class": "frase fr"})
        phrases = []
        for tags in frase_fr_class:
            phrases.append(tags.text)
        return phrases
    
    def getAllPhrasesFromSite(self):
        cont = 1
        url_increment = ''
        first_result = self.getPhrasesFromUrl(self.url)
        last_result = []
        all_phrases = []
        while first_result != last_result:
            new_url = self.url+url_increment
            print('Extraindo de: ',new_url)
            new_phrases = self.getPhrasesFromUrl(new_url)
            all_phrases = all_phrases+new_phrases
            cont+=1
            url_increment = str(cont)+'/'
            if cont > 2:
                last_result = new_phrases
        return all_phrases


crawler = PensadorCrawler()
frases = crawler.getAllPhrasesFromSite()

print(len(frases))