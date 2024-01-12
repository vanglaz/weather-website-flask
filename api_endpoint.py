import requests
import jsons

city_name = "Vientiane"
api_key = "33a7737e12f5c3f8bb50e99180cbd845"

api_endpoint = "http://api.openweathermap.org/data/2.5/weather?"
query_params = {"q": city_name, "appid": api_key, "units": "metric"}

# query_params = {"appid": api_key}

response = requests.get(api_endpoint, params=query_params)

if response.status_code == 200:
    print("Succusful Acessed API:", response.status_code)
    data = response.json()
    print(data["coord"]["lon"])
    # Handle response data
    temperature = data["main"]["temp"]
    print(f"In {city_name} is temperature: {temperature} °C")
else:
    # Handle errors
    print(f"Error: {response.status_code} - {response.text}")
