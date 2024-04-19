
import requests
from bs4 import BeautifulSoup     
from urllib import parse          

def search(search):
  url = "https://www.google.com/search?tbm=nws&q=" + parse.quote(search)
  res = requests.get(url, timeout=5)
  soup = BeautifulSoup(res.text, "html.parser")
  list_news = soup.findAll("div", {"class":"Gx5Zad fP1Qef xpd EtOod pkphOe"})
  print("검색어 관련 뉴스(구글) 10개를 가져왔습니다!")
  for x in list_news:
    title= x.find("div", {"class":"BNeawe vvjwJb AP7Wnd"}).get_text()
    print()
    print(title)
    href = x.find("a")['href'][7:]
    print(href)

def getRecent(search):
    url = "https://www.google.com/search?tbm=nws&q=" + parse.quote(search)
    res = requests.get(url, timeout=5)
    soup = BeautifulSoup(res.text, "html.parser")
    list_news = soup.findAll("div", {"class":"Gx5Zad fP1Qef xpd EtOod pkphOe"})
    if list_news:
        first_news_title = list_news[0].find("div", {"class":"BNeawe vvjwJb AP7Wnd"}).get_text()
        print()
        print("※--------------------------가장 최근에 업로드된 뉴스의 제목--------------------------※")
        print("---짜잔~!♥--->",first_news_title)
       

    else:
        print("No news found.")
