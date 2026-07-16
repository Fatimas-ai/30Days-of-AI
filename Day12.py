import requests
url="https://jsonplaceholder.typicode.com/posts"
print(requests.get(url))

import requests
url="https://jsonplaceholder.typicode.com/posts"
print(requests.get(url).status_code)
print(requests.get(url).text)

import requests
url="https://jsonplaceholder.typicode.com/users"
print(requests.get(url).json())

import requests
url="https://jsonplaceholder.typicode.com/users"
data={
    "name":"fatima",
    "grade":"a"
}
response=requests.get(url)
data=response.json()
print(data[0]["name"])

import requests
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "Python",
    "body": "Learning API",
    "userId": 1
}
response=requests.post(url,json=data)
print(response.json())


