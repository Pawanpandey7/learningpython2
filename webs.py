# web scraping 
#importing the requests library to make HTTP requests
import requests

#Importing BeautifulSoup from bs4 to parse html content
from bs4 import BeautifulSoup

#define a function to get weather for a given city
def get_weather(city):
    #convert the city to lowercase and replace spaces with hyphens
    city = city.lower().replace(" ", "-")

    #build th efull url of the weather app
    url =f"https://www.timeanddate.com/weather/{city}"

    #send an HTTP GET request for the weather page
    response = requests.get(url)

    #if the request dails show error and stop
    if response.status_code != 200:
        print("failed to retrieve data")
        return

    #parse the html content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    #find the first <div> tag with class 'h2' which contains temperature info
    temp = soup.find("div",class_="h2").text.strip()

    #find the first <p> tag which typically contains the weather condition
    condition = soup.find("p").text.strip()


    #print the formateed city name and the scraped weather information
    print(f"weather in {city.replace('-',' ').title()}:")
    print(f"temperature: {temp}")
    print(f"Condition: {condition}")

#call the funtion with "Nepal/Kathmandu" as an example
get_weather("Nepal/Kathmandu")


