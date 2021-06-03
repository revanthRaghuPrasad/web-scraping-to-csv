import requests
from bs4 import BeautifulSoup
import pandas as pd

# response = requests.get("https://api.github.com")
# print(response.content.decode('utf-8'))
# print(response.json())

response = requests.get("https://forecast.weather.gov/MapClick.php?lat=34.053570000000036&lon=-118.24544999999995#.YLiZzKgzZPY")

soup = BeautifulSoup(response.content, "html.parser")
week = soup.find(id="seven-day-forecast-body")

items = week.find_all(class_="tombstone-container")

# print(items[0].find(class_="period-name").get_text())
# print(items[0].find(class_="short-desc").get_text())
# print(items[0].find(class_="temp").get_text())


period_names = [item.find(class_="period-name").get_text() for item in items]
short_descriptions = [item.find(class_="short-desc").get_text() for item in items]
temperatures = [item.find(class_="temp").get_text() for item in items]
# print(period_names)
# print(short_descriptions)
# print(temperatures)

weather_data = pd.DataFrame(
    {
        'Period' : period_names,
        'Short descriptions' : short_descriptions,
        'Temperatures' : temperatures
    }
)
print(weather_data)

weather_data.to_csv("weather.csv")