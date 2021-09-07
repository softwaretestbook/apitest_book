#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/3 17:43
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : 4-2.py
# @Software: PyCharm
import requests

url = 'http://127.0.0.1:12356/dif'
param = {'diff':'1'}

res_get = requests.get(url,params=param)
print(res_get.text)
print(res_get.url)