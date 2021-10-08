#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   test_index.py
@Time    :   2021/09/28 14:10:13
@Author  :   CrissChan 
@Version :   1.0
@Site    :   https://blog.csdn.net/crisschan
@Desc    :   主页接口
'''
from unittest import TestCase
import unittest
from unittest.main import main
import requests

class TestIndex(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    def tearDown(self) -> None:
        return super().tearDown()
    def test_index(self):
        url = 'http://127.0.0.1:12356'
        res_index = requests.get(url)

        self.assertEqual(res_index.status_code,requests.codes.ok,msg="返回状态码是200")
        self.assertIn('username',res_index.text,msg='response include username')



# if __name__ == '__main__':
#     unittest.main()
