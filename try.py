import requests
from bs4 import BeautifulSoup
temp = requests.get("https://www.onlinekhabar.com/")

if temp.status_code != 200:
    print("couldnot")

else:
    print(temp)
    temp2 = BeautifulSoup(temp.text,'html.parser')
    news =temp2.find('section', class_='ok-bises ok-bises-type-2') \
                .find('div', class_='ok-container') \
                .find('h2') \
                .find('a').text.strip()
    print(news)


