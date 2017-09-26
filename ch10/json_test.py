import json

json_string = '{"first": "Emmett", "last": "Brown", "prefix": "Dr."}'

name = json.loads(json_string)

print(name['prefix'], name['first'], name['last'])
