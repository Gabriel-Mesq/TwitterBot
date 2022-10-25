import requests
import datetime

def weather(city):
    
    API_KEY = " "
    request_url = f"https://api.openweathermap.org/data/2.5/weather?&q={city}&appid={API_KEY}"
    response = requests.get(request_url)

    #Code 200 = Sucess
    if response.status_code == 200:
        data = response.json()
        description = data['weather'][0]['description']
        temperature = round(data["main"]["temp"] - 273.15, 2)
    else:
        print("An error occurred.")

    current_time = datetime.datetime.now()

    return f"Clima do país {city} no dia {current_time.day}/{current_time.month}/{current_time.year}, às {current_time.hour}:{current_time.minute}:\n{temperature}°C - {description}"

