from bs4 import BeautifulSoup
import requests

# url = "https://piratebayorg.net/search.php?q=vikings&cat=0"
# result = requests.get(url).text

with open("torrent.html", "r") as f:
    result = f.read()


soup = BeautifulSoup(result, "html.parser")
entries = soup.find_all(id="st")
name = entries[0].find(class_="list-item item-name item-title").a.text
size = entries[0].find(class_="list-item item-size").text
link = entries[0].find(class_="item-icons").a['href']

payload = f"Name: {name}\nSize: {size}\nLink: {link}"

print(payload)