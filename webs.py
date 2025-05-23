# web scraping 
import requests 
from bs4 import BeautifulSoup

def get_weather(city):
    city = city.lower().replace(" ", "-")
    url =f"https://www.timeanddate.com/weather/{city}"

    response = requests.get(url)
    if response.status_code != 200:
        print("failed to retrieve data")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    temp = soup.find("div",class_="h2").text.strip()
    condition = soup.find("p").text.strip()

    print(f"weather in {city.replace('-',' ').title()}:")
    print(f"temperature: {temp}")
    print(f"Condition: {condition}")

#example usage
get_weather("Nepal/Kathmandu")
        

