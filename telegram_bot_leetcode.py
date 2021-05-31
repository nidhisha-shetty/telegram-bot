import requests
import time
messages=["Solve a Leetcode problem anytime today","It's been half day hope you have already attempted to solve a leetcode problem","Nidhisha, hope you got the solution to the leetcode problem"]
for message in messages:
	base_url="https://api.telegram.org/bot1806647189:AAE2Edo2Vk804YuQqMV2cWGqm3pjdNedFfE/sendMessage?chat_id=-501831801&text=\"{}\"".format(message)
	requests.get(base_url)
	time.sleep(21600)