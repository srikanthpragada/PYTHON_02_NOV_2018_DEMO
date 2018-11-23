import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()

for country in countries:
    print(f"{country['name']:50s}  {country['capital']:20s}  {country['population']}")


