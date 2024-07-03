import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
}

city_name = input()
weather_url = 'http://wthrcdn.etouch.cn/weather_mini?city={}'.format(city_name)
city_response = requests.get(weather_url, headers=headers)
weather_dict = json.loads(city_response.text)
print(type(weather_dict))
print(weather_dict)
