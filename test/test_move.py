import requests
from pprint import pprint

# /move
url = "http://127.0.0.1:8000"
endpoint = "/move"
json = {"matchId":2, "playerId":"X", "square":{"x":3, "y":2}}
operation = requests.post
response = operation(f"{url}{endpoint}",json=json)
pprint(response.__dict__)
pprint(response.status_code)
pprint(response.json())
