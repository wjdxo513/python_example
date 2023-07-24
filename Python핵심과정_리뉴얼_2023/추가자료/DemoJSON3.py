import json
from pprint import pprint

s = '''{
    "test": [
        {
            "customer": "test1",
            "type": [
                "windows"
            ],
            "contact": [{
                "name": "a",
                "email": "@gmail.com",
                "phone": null ,
                "remarks": null
            }]
        },
        {
            "customer": "test2",
            "type": [
                "android"
            ],
            "contact": [{
                "name": "b",
                "email": "@gmail.com",
                "phone": "010-0000-0000",
                "remarks": null
            }]
        },
        {
            "customer": "test3",
            "type": [
                "android"
            ],
            "contact": [{
                "name": "a",
                "email": "@naver.com",
                "phone": null,
                "remarks": null
            }]
        }
    ]
}'''

d = json.loads(s)
print('------')

pprint(d)
print('------')

for e in d['test']:
    pprint(e['contact'])
print('------')

for i, e in enumerate(d['test']):
    print(i, e['contact'][0]['email'])
print('------')

emails = { e['contact'][0]['email'] for e in d['test']}
print(emails)
print('------')