import requests
from pprint import pprint as pp
import json

owner = 'DmitriiKozhakin'

# /repos/{owner}/{repo}

r = requests.get(f'https://api.github.com/users/{owner}/repos')
r_json = r.json()


path = "HW_1_1.json"
with open(path, 'w') as f:
    json.dump(r_json, f, indent=2)