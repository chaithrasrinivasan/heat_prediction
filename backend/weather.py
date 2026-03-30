import requests

API_KEY = "7c9d285a27bb53b0da08b1b8417bca0e"

def get_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    
    res = requests.get(url).json()

    print("FULL RESPONSE:", res)   # 👈 ADD THIS

    temp = res['main']['temp']
    humidity = res['main']['humidity']
    
    return temp, humidity