import requests
from pprint import pprint
# 1) /move
url = "http://127.0.0.1:8000"
endpoint = "/move"
body = {"matchId":1, "playerId":"X", "square":{"x":1, "y":-1}}
operation = requests.post
response = operation(f"{url}{endpoint}",json=body)
pprint(response.headers)
pprint(response.status_code)
pprint(response.json())

# 2) /status
url = "http://127.0.0.1:8000"
endpoint = "/status"
query = "?matchId=1"
params = {"matchId":1}
operation = requests.get
response = operation(f"{url}{endpoint}{query}")
pprint(response.__dict__)
pprint(response.status_code)
pprint(response.json())

# 3) /create
url = "http://127.0.0.1:8000"
endpoint = "/create"
operation = requests.post
response = operation(f"{url}{endpoint}")
pprint(response.__dict__)
pprint(response.status_code)
pprint(response.json())