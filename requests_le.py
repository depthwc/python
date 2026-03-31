import requests

# r = requests.get("https://example.com/")

# print(r.content)


# import requests

# r = requests.get('https://api.github.com/events')
# print(r.json())


# r = requests.get("https://example.com/", stream = True)



# r = requests.put('https://httpbin.org/put', data={'key': 'value'})
# print(r.text)


# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1'}

# r = requests.get(url, headers=headers)
# print(r.text)

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)
{
  "form": {
    "key2": "value2",
    "key1": "value1"
  },
}