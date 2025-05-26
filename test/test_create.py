import requests
from pprint import pprint

# /create
url = "http://127.0.0.1:8000"
endpoint = "/create"
operation = requests.post
data = None
response = operation(f"{url}{endpoint}", data=data)
pprint(response.__dict__)
pprint(response.status_code)
pprint(response.json())

url = "http://127.0.0.1:8000"
endpoint = "/create"
operation = requests.post
json = {
    "id":900,
    "turn":"X",
    "board":"_________"
}
response = operation(f"{url}{endpoint}", json=json)
pprint(response.__dict__)
pprint(response.status_code)
pprint(response.json())

url = "http://127.0.0.1:8000"
endpoint = "/create"
operation = requests.post
json = {
    "turn":"O",
    "board":"_________"
}
response = operation(f"{url}{endpoint}", json=json)
pprint(response.__dict__)
pprint(response.status_code)
pprint(response.json())