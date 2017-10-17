import requests, json

url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(url)

if (response.status_code == 200):
    response_dictionary = json.loads(response.text)
    position = response_dictionary['iss_position']
    print('International Space Station at ' +       
        position['latitude'] + ', ' + position['longitude'])
else:
    print("Houston, we have a problem:", response.status_code)
