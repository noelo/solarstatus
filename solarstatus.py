import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
import re
import json

URL = 'http://192.168.4.99/status.html'
page = requests.get(URL,auth=('admin', 'admin'))

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all(["script"])[1].string
p = re.compile("var webdata_[t|n][a-z_]* = .*;")
vars = p.findall(results)
dict = {}
for var in vars:
    li = var.split(' ')
    dict[li[1]] = li[3].replace(';','').replace('"','')
print(json.dumps(dict))