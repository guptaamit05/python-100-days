import requests, json


# response = requests.get("http://api.open-notify.org/iss-now.json")
# if response.status_code == 200:
#     print(response.json())

# else: 
#     print("no response found..")

LATITUDE=22.357379
LONGITUDE=75.934582

parameters = {
    'lat': LATITUDE,
    'lng': LONGITUDE
}

try:
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']

    print(f"Sunrise: {sunrise}\nSunset:{sunset}")

except Exception as e:
    print(f"Error: {e}")



