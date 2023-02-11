import requests
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "2cdcfa971a0a2fe0c08b38950bae10db"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)
# URL = "http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json"
# response = requests.get(endpoint)
# if response.status_code == 200:
#     data = response.json()
# print("Keys in the JSON object:")

# for key in data.keys():
#     print(key)


def main():
    temp = get_weather("London")
    print(temp)

if __name__ == "__main__":
    main()
