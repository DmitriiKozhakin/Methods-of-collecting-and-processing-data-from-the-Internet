import requests
from pprint import pprint as pp
import json

method_name = 'users.get'
v = '5.130'

access_token = "21bd0f6d03b18813304bf4155c9dd9704e4f1abea76ebaebd92c48de6a52e6cb79c345c79e0476cb7c541"

r = requests.get(f'https://api.vk.com/method/{method_name}?PARAMETERS&access_token={access_token}&v={v}')
r_json = r.json()
path = "HW_1_2.json"
with open(path, 'w') as f:
    json.dump(r_json, f, indent=2)



