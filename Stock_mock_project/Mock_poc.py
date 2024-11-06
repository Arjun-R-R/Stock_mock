import requests
import pandas as pd
api_url = ("https://api.json-generator.com/templates/jXRA8JJfFA-K/data?access_token=kyff6fnu2qeur5ycji753t31ay5o7hi8l72asnxm")
response = requests.get(api_url)
#print(response)
a = response.json


