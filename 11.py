# -*- coding: UTF-8 -*-
from urllib import requests
import io

response = request.urlopen("http://www.fanyi.baidu.com/")
html = response.read()
html = html.decode("utf-8")
f = io.open(r'C:\Users\Andy\Desktop\html.txt', 'w',encoding='utf-8')
f.write(html)
f.close()
print('鍐欏叆鎴愬姛')
