import requests
import json


r = requests.get('https://api.github.com')

print(r.content)