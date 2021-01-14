import aiogram


import requests

API_link = "https://api.telegram.org/bot1528537552:AAFiUgQ49InBRihL2RH3gi95pcD9mwVmJ-I"

updates = requests.get(API_link + "/getUpdates?offset=-1").json()

print(updates)

message = updates["result"][0]["message"]

chat_id = message["from"]["id"]
text = message["text"]

sent_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text=Привет, ты написал {text}")
