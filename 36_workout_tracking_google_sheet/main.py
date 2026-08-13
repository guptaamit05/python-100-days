import requests, os, json
from dotenv import load_dotenv

load_dotenv()

BASE_URL="https://app.100daysofpython.dev"
APP_ID=os.getenv("APP_ID")
APP_KEY=os.getenv('APP_KEY')
#  Add Data..............

add_endpoint = f"{BASE_URL}/v1/nutrition/natural/exercise"
headers ={
    'Content-Type':'application/json',
    'x-app-id':APP_ID,
    'x-app-key':APP_KEY
}

add_params ={
    # 'query':"me and my friend daily go to gym for 1hour",
    # 'query':"I am writing a letter from last 30 minutes",
    'query':"I am dancing from last 3 hours",
    'age':35,
    'gender':'male',
}

res = requests.post(url=add_endpoint, headers=headers, json=add_params)
print(res.json())