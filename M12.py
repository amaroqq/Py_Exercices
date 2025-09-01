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
#Task 2
munic = input("Enter municipality name: ")
apikey='placeholder'
#no real key yet
req = f"http://api.openweathermap.org/geo/1.0/direct?q={munic}&limit=5&appid={apikey}"
try:
    rp = requests.get(req)
    # print(json.dumps(rp.json(), indent=2))
    if (rp.status_code==200):
        print("im here")
        rpjson=rp.json()
        latm = rpjson["lat"]
        lonm = rpjson["lon"]
        req=f"https://api.openweathermap.org/data/3.0/onecall?lat={latm}&lon={lonm}&appid={apikey}"
        try:
            rp = requests.get(req)
            if (rp.status_code==200):
                rpjson=rp.json()
                print(f'Weather outside is {rpjson["weather"]["description"]}, temperature is {rpjson["main"]["temp"]}')
        except requests.exceptions.RequestException as e:
            print("Request couldn't be completed")
except requests.exceptions.RequestException as e:
    print("Request couldn't be completed")