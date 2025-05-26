import requests
from pprint import pprint

# Trying to move on a un-finished match, when is your turn, on a free square
url = "http://127.0.0.1:8000"
endpoint = "/move"
json = {"matchId":2, "playerId":"X", "square":{"x":3, "y":2}}
operation = requests.post
response = operation(f"{url}{endpoint}",json=json)
pprint(response.__dict__)
pprint(response.status_code)
pprint(response.json())

# Trying to move in a finished match
url = "http://127.0.0.1:8000"
endpoint = "/move"
json = {"matchId":5, "playerId":"X", "square":{"x":3, "y":2}}
operation = requests.post
response = operation(f"{url}{endpoint}",json=json)
pprint(response.__dict__)
pprint(response.status_code)
pprint(response.json())

# Trying to move on a un-finished match, when is NOT your turn
url = "http://127.0.0.1:8000"
endpoint = "/move"
json = {"matchId":2, "playerId":"X", "square":{"x":3, "y":2}}
operation = requests.post
response = operation(f"{url}{endpoint}",json=json)
pprint(response.__dict__)
pprint(response.status_code)
pprint(response.json())

# Trying to move on a un-finished match, when is your turn, NOT on a free square
url = "http://127.0.0.1:8000"
endpoint = "/move"
json = {"matchId":2, "playerId":"X", "square":{"x":3, "y":2}}
operation = requests.post
response = operation(f"{url}{endpoint}",json=json)
pprint(response.__dict__)
pprint(response.status_code)
pprint(response.json())
