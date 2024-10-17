# Will be creating some project to check weather
import requests
api_key="34f571b67dd215c8558d75dca370ec75"

def get_data(city_name):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        return data        
    else:
        print(f"Failed To Retreive Weather Data {response.status_code}")

city_name=input("Enter City Name (Otherwise i will consider similar city ): ")

raw_data=get_data(city_name)
if raw_data:
    print(f"Wind Speed in {raw_data["name"]} is  {raw_data["wind"]["speed"] } Kmph")
    print(f"{raw_data["weather"][0]["main"]}: {raw_data["weather"][0]["description"]}")
    fahrenheit_temp =raw_data["main"]["temp"]
    celsius_temp=(fahrenheit_temp-32)*(5/9)
    print(f"Temperature in {raw_data["name"]} ({raw_data["sys"]["country"]}) is {celsius_temp:.2f} Celsius")
    print(f"Sea level for {raw_data["name"]} is  {raw_data["main"]["sea_level"]} feets above sea level ")
    
