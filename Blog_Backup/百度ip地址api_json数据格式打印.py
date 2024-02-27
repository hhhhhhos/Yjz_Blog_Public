import requests
import json

ip = "192.241.199.88"
location = "Unknown"
# json转字典
response_json = requests.get(f"https://opendata.baidu.com/api.php?query={ip}&co=&resource_id=6006&oe=utf8").json()
# 字典美化
#response = json.dumps(response_json, indent=4,ensure_ascii=False)
# 字典取值 空返回None 不取
if response_json.get("data"):
    location = response_json.get("data")[0]["location"]



