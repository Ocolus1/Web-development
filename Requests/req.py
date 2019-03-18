import requests
req = requests.get('http://facebook.com')
print(req.encoding)
print(req.status_code)
print(req)
print(req.headers)
print(req.headers['Content-Encoding'])
print(req.elapsed)
print(req.history)
# print(req.text)
# print(req.content)
print(req.raw)


import requests
query = {'q': 'Forest', 'order': 'popular', 'min_width':'800', 'min_height':'600'}
req = requests.get('https://pixabay.com/en/photos/', params=query)
print(req.url)


import requests
req = requests.post('https://en.wikipedia.org/w/index.php', data = {'search':'Nanotechnology'})
req.raise_for_status()
with open('Nanotechnology.html', 'wb')as fd:
    for chunk in req.iter_content(chunk_size=50000):
        fd.write(chunk)