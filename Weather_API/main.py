import requests
from pprint import pprint

API_Key = '2545ffa2ee88e4239af2ab606c109af6'

city = input("Enter a City Name: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?apppid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
