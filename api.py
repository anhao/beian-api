import requests

url = "https://icp.dwz.today/free/icp/name?name=E5%8C%97%E4%BA%AC%E5%8C%97%E6%AF%94%E4%BF%A1%E6%81%AF%E6%8A%80%E6%9C%AF%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
