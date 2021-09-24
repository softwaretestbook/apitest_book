#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/3 17:43
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : 4-2.py
# @Software: PyCharm
import requests
import json
## get
print('--------get-------')
url = 'http://127.0.0.1:12356'## ##
res_index = requests.get(url)
if res_index.status_code == requests.codes.ok:
    print(requests.codes.ok)
print(res_index.text)
print(res_index.status_code)
print(res_index.headers)


print(res_index.headers['Content-Type'])
print(res_index.headers['content-type'])
print(res_index.headers.get('Content-Type'))
print(res_index.headers.get('content-type'))
## get--headers
print('--------get-headers------')
url = 'http://127.0.0.1:12356'
headers = {'Host': '127.0.0.1',
'Connection': 'keep-alive',
'Content-Type': 'text/plain',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'X-usrg': 'criss'}
res_index = requests.get(url,headers = headers)
print(res_index.text)
print(res_index.status_code)
print(res_index.headers)
## get_param
print('--------get_param-------')
url_diff = 'http://127.0.0.1:12356/diff'
payload = {'diff':'easy'}
res_diff = requests.get(url_diff,params=payload)

print(res_diff.text)
print(res_diff.status_code)
print(res_diff.headers)

## post
print('--------post-------')
url_login = 'http://127.0.0.1:12356/login'
username='CrissChan'
password='CrissChan'
payload = {'username': username,'password':password}
res_login = requests.post(url_login,data=json.dumps(payload))

print(res_login.cookies['username'])
print(res_login.text)
print(res_login.status_code)
print(res_login.headers)

## ReqeustsCookieJar

cookie_jar = requests.cookies.RequestsCookieJar()
cookie_jar.set('JSESSIONID', '23A15FE6655327749BC822A79CF77198', domain='127.0.0.1', path='/')
url = 'http://127.0.0.1:12356'
r = requests.get(url, cookies=cookie_jar)
