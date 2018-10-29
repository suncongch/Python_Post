import requests
import io
import re

def get_img():
    res_tr = r'data-src=(.*?)>'
    m_tr = re.findall(res_tr, res.text, re.S | re.M)
    for line in m_tr:
        print line
        f.write(('<img src=')+line+('>\n\r'))
def get_title():
    res_tr = r'<title>(.*?)</title>'
    m_tr = re.findall(res_tr, res.text, re.S | re.M)
    for line in m_tr:
        print line
        f.write(('<p>')+line+('</p>\n\r'))
def get_text():
    res_tr = r'<h4>(.*?)</h4>'
    m_tr = re.findall(res_tr, res.text, re.S | re.M)
    for line in m_tr:
        print line
        f.write(('<p>')+line+('</p>\n\r'))
        break
def get_text1():
    res_tr = r'<div class="c"></div>(.*?)<input'
    m_tr = re.findall(res_tr, res.text, re.S | re.M)
    for line in m_tr:
        #print line
        res_tr = r'<div class="c"></div>(.*?)<input'
        m_tr1 = re.findall(res_tr, line+('<input'), re.S | re.M)
        for line1 in m_tr1:
            print line1
            f.write(('<p>')+line1+('</p>\n\r'))
            break
        break

url = 'http://www.t66y.com/htm_data/16/1810/3287898.html'
head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
     }
request = requests.get(url,
                       headers=head,
                       verify=False)
res = requests.post(url, headers=head)
res.encoding = res.apparent_encoding
#res_tr = r'data-src=(.*?)>'
#res_tr = r'<title>(.*?)</title>'
#m_tr = re.findall(res_tr, res.text, re.S | re.M)
f = io.open(r'C:\Users\Andy\Desktop\html.txt', 'w',encoding='utf-8')
get_title()
get_text()
get_text1()
get_img()
f.write(res.text)
f.close()
print('success')
#return res.text

