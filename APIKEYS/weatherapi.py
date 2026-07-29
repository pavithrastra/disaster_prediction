import requests

API_KEY = "c34affd06e1b1d0f71e0db2f42921f2c"
city = "Chennai"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
#data = response.json()

#print(data) 
