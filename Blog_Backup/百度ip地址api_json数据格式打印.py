import requests
import json

response_json = requests.get("https://opendata.baidu.com/api.php?query=61.140.126.70&co=&resource_id=6006&oe=utf8").json()
response = json.dumps(response_json, indent=4)
print(response)
