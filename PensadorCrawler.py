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
        file = open("pensadorPhrases.txt", "r")
        phrases_cache = file.readlines()
        file.close()
        for tags in frase_fr_class:
            new_phrase = tags.text
            phrases.append(new_phrase)
            if new_phrase+'\n' not in phrases_cache:
                file = open("pensadorPhrases.txt", "a")
                file.write("%s\n" % new_phrase)
                print("Adicionando Frase... ")
                file.close()
        return phrases
    
    def getAllPhrasesFromSite(self):
        cont = 1
        url_increment = ''
        first_result = self.getPhrasesFromUrl(self.url)
        last_result = []
        all_phrases = []
        while first_result != last_result:
            new_url = self.url+url_increment
            file = open("siteCache.txt", "r")
            site_cache = file.readlines()
            file.close()
            if new_url+'\n' not in site_cache:
                print('Extracting from: ',new_url)
                new_phrases = self.getPhrasesFromUrl(new_url)
                file = open("siteCache.txt", "a")
                file.write("%s\n" % new_url)
                file.close()
                all_phrases = all_phrases+new_phrases
                if cont > 2:
                    last_result = new_phrases
            cont+=1
            url_increment = str(cont)+'/'

        return all_phrases
        

crawler = PensadorCrawler()
all_phrases = crawler.getAllPhrasesFromSite()