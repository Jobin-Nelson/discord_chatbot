import requests
from bs4 import BeautifulSoup
from pprint import pprint

def main():
    url = "https://piratebayorg.net/search.php"
    headers ={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.53",
              "authority": "piratebayorg.net",
              "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
              }
    params = {"q":"vikings", "cat":0}

    r = requests.get(url, params=params)
    soup = BeautifulSoup(r.text, 'html.parser')

    pprint(soup)

if __name__=="__main__":
    main()
