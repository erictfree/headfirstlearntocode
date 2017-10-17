import requests

url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(url)

if (response.status_code == 200):
    print(response.text)
else:
    print("Houston, we have a problem:", response.status_code)
