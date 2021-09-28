#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   test_login.py
@Time    :   2021/09/28 17:28:49
@Author  :   CrissChan 
@Version :   1.0
@Site    :   https://blog.csdn.net/crisschan
@Desc    :  登录接口
'''
from unittest import TestCase
import requests
import json
class TestLogin(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    def tearDown(self) -> None:
        return super().tearDown()
    def test_login(self):
        url_login = 'http://127.0.0.1:12356/login'
        username='CrissChan'
        password='CrissChan'
        payload = {'username': username,'password':password}
        res_login = requests.post(url_login,data=json.dumps(payload))
        print(res_login.text)
        print(res_login.status_code)
        print(res_login.headers)

