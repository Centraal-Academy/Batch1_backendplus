import asyncio
import urllib.request

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

async def get_request(url):
    request = await urllib.request.urlopen(url)
    return request

async def read_data(request):
    response = request.read()
    return response

async def call_url(url):
    print('Starting {}'.format(url))
    response = await get_request(url)
    data =  await read_data(response)
    print('{}: {} bytes: {}'.format(url, len(data), data))
    return data

futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
new_data = loop.run_until_complete(asyncio.wait(futures))
print("ya termine absolutamente todo")
