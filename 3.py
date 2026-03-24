import re
r = re.findall(r'\b\w\d{3}\b', "a123 b45 c678 d901")

print(r)