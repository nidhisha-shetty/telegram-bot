import requests
import time
messages=["Nidhisha, solve a leetcode problem today"]
for message in messages:
	base_url="https://api.telegram.org/bot1806647189:AAE2Edo2Vk804YuQqMV2cWGqm3pjdNedFfE/sendMessage?chat_id=-501831801&text=\"{}\"".format(message)
	requests.get(base_url)
	
