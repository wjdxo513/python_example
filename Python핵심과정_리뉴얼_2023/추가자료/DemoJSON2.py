import json
from io import StringIO

io = StringIO('{"title": "Book1", "ISBN": "12345", "author": [{"name": "autho1", "age": 30}, {"name": "autho2", "age": 25}]}')
json_data = json.load(io)

print(json_data['title'])
print(json_data['ISBN'])

for author in json_data['author']:
    print(author['name'])
    print(author['age'])

#파이썬 형식을 JSON으로 변환
book = {'title': 'Book1', 'ISBN': '12345', 'author': [{'name': 'autho1', 'age': 30}, {'name': 'autho2', 'age': 25}]}
print(json.dumps(book))
print('')
print(json.dumps(book, indent=4))