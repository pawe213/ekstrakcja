import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

ptodos = ''
a = str(todos[0])
print(a.strip('{'))

for slownik in todos:
    ptodos = ptodos + str(slownik).strip('{').strip('}').replace("'", '') + '\n'

print(ptodos)

for slownik in todos:
    if slownik['completed'] == False and slownik['userId'] == 1:
        print(str(slownik).strip('{').strip('}').replace("'", ''))

response = requests.get("http://api.nobelprize.org/v1/prize.json")
nobels = json.loads(response.text)['prizes']


for nagroda in nobels:
    if nagroda['year'] == '2014' and nagroda['category'] == 'peace':
        for ziomek in nagroda['laureates']:
            print(ziomek['firstname'] + ' ' + ziomek['surname'])

for nagroda in nobels:
    if nagroda['year'] == '2019':
        print(nagroda['category'].upper())
        for ziomek in nagroda['laureates']:
            print('   ' + ziomek['firstname'] + ' ' + ziomek['surname'])