import requests

url  = "https://httpbin.org/post"

data = {"name":"rpa_ai","age":"30"}

res = requests.post(url,json=data)

print(res.status_code)
print(res.json())