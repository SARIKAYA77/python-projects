import requests
from bs4 import BeautifulSoup

url ="https://www.doviz.com"

response = requests.get(url)



data = response.text
soup = BeautifulSoup(data, 'html.parser')



money = soup.find_all("span", {"class": "value"})
names = soup.find_all("span", {"class": "name"})

for mo,na in zip(money, names):
    print("değeri", mo.text)

    print("dövizin adı", na.text)

url = "https://www.imdb.com/chart/top"

response = requests.get(url)


data = response.content

soup = BeautifulSoup(data,"html.parser")

baslıklar = soup.find_all("td",{"class":"titleColumn"})

ratingler = soup.find_all("td",{"class":"ratingColumn imdbRating"})


for baslık, rating in zip(baslıklar ,ratingler):
    print("başlık",baslık.text)

    print("puan", rating.text)

