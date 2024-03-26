import requests

BASE = 'http://127.0.0.1:5000/'

data = [{"likes": 10, "name": "Joe", "views": 100},
        {"likes": 100, "name": "John", "views": 1000},
        {"likes": 1000, "name": "Jack", "views": 10000}]

for i in range(len(data)):
    response = requests.put(BASE + 'video/' + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + 'video/0')
print(response)

input()
response = requests.get(BASE + 'video/2')
print(response.json())