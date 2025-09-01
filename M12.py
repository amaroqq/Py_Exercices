import requests
import json
#Task 1
req = "https://api.chucknorris.io/jokes/random"
try:
    rp = requests.get(req)
    if (rp.status_code==200):
        rpjson=rp.json()
        print(rpjson["value"])
except requests.exceptions.RequestException as e:
    print("Request couldn't be completed")