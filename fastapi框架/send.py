import requests





re = requests.post("http://localhost:6000/messages")

print(re.json())