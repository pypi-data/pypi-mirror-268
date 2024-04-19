import requests
import json

url = "http://127.0.0.1:30001/SendTextMsg_NoSrc"
url = "http://218.0.55.172:30001/SendTextMsg_NoSrc"
payload = json.dumps({
    "wxidorgid": "swangwh",
    "msg": "你收不到消息么--来自接口"
})
headers = {
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, params=payload)

print(response.text)
