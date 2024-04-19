
import requests
from bs4 import BeautifulSoup     #pip install bs4
from urllib import parse           #pip install urllib
def search(search):
  url = "https://www.google.com/search?tbm=nws&q=" + parse.quote(search)
  res = requests.get(url, timeout=5)
  soup = BeautifulSoup(res.text, "html.parser")
  list_news = soup.findAll("div", {"class":"Gx5Zad fP1Qef xpd EtOod pkphOe"})
  for x in list_news:
    title= x.find("div", {"class":"BNeawe vvjwJb AP7Wnd"}).get_text()
    print()
    print(title)
    href = x.find("a")['href'][7:]
    print(href)

def print_what(search):
    print(search)
