import requests
from pprint import pprint
# 
url = "http://127.0.0.1:8000"
endpoint = "/status"
params = {"matchId":1}
operation = requests.get
response = operation(url=f"{url}{endpoint}", params=params)
pprint(response.__dict__)
pprint(response.status_code)
pprint(response.json())

url = "http://127.0.0.1:8000"
endpoint = "/status"
params = {"matchId":12}
operation = requests.get
response = operation(url=f"{url}{endpoint}", params=params)
pprint(response.__dict__)
pprint(response.status_code)
pprint(response.json())

