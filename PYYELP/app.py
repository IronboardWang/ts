import requests
import congfig
url = "https://api.yelp.com/v3/businesses/search"
#api_key = "jsaS-455bNLPYnf32rCSZwKa7db1t9ExrSevbS0sAUhfaJX5iWPVqzaPm-vJz49jZnwVAFoZomfQH5WGF2ptLJuHwVyAQC3kZrstfuc9sDAUyHCF3tecqjXqPrbgXnYx"
headers = {
    "Authorization" : "Bearer "+ congfig.api_key
}
params = {
    "term" : "Barber",
    "location" : "NYC" 
}
response = requests.get(url, headers=headers,params=params)
businesses = response.json()["businesses"]
names = [business["name"] for business in businesses if business["rating"] > 4.5]
print(names)
