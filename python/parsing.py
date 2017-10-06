import urllib.request
import urllib.parse
import re

url  = "http://centraal.academy"

resp = urllib.request.urlopen(url)
data = resp.read()

p = re.findall(r'<p>(.*?)</p>', str(data))  
h = re.findall(r'<h2>(.*?)</h2>', str(data))  

for item in p:
    print(item)

for item in h:
    print(item)