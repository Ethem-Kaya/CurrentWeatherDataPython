import requests
import os 
from datetime import datetime
while True:

    User_Api= "68b9c4cf6ccdf50752f94796f3093734"
    location=input("Enter the city: ")

    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+User_Api

    api_link = requests.get(complete_api_link)

    api_data = api_link.json()

    
    temp_city=((api_data["main"]["temp"])-273.15)
    weather_descprition=api_data["weather"][0]["description"]
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']

    print ("Current temperature is: {:.2f} deg C".format(temp_city))
    print ("Current weather desc  :",weather_descprition)
    print ("Current Humidity      :",hmdt, '%')
    print ("Current wind speed    :",wind_spd ,'kmph')