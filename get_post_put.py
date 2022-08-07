import requests

image = requests.get('https://i0.wp.com/mcsjournal.ru/wp-content/uploads/2020/12/1412img-1-1.png?resize=1024%2C625&ssl=1')
with open('new_image.png', 'wb') as f:
    f.write(image.content)
data = {
    "title": "заголовок",
    "body": "тест в теле  для теста реквест",
    "userId": 1,
}
headers = {
    "Content-type": "application/json; charset=UTF-8"
}
print('================================================================================================')

print('запрос get =>' )
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print('статус код', r.status_code)
print(r.headers['content-type'])
print('кодировка',r.encoding)
print('текстовый файл', r.text)
print('файл  в формате json', r.json())

print('================================================================================================')

print('запрос put =>' )
r = requests.put('https://my-json-server.typicode.com/typicode/demo')
print('---статус код', r.status_code)
print('-----', r.headers['content-type'])
print('------кодировка',r.encoding)
print('-------текстовый файл', r.text)
print('файл  в формате json', r.json())

print('================================================================================================')

r = requests.head('https://my-json-server.typicode.com/typicode/demo/posts', auth=('user', 'pass'))
print('статус код--------', r.status_code)
print('текстовый файл--------', r.text)
print('================================================================================================')

# json, data
r1 = requests.post(
    "https://my-json-server.typicode.com/typicode/demo/posts",
    headers=headers,
    json=data
)
print('запрос post', r1.json())

print('================================================================================================')


