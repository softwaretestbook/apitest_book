#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   test_suiteone.py
@Time    :   2021/09/29 10:37:07
@Author  :   CrissChan 
@Version :   1.0
@Site    :   https://blog.csdn.net/crisschan
@Desc    :   None
'''

from json import loads
import unittest
from HTMLTestRunner import HTMLTestRunner
from test_caseone import TestOne
from test_index import TestIndex
from test_login import TestLogin

suite = unittest.TestSuite()
loader = unittest.TestLoader()
# 方法1 一条一条的将TestCase加入TestSuite
case1 = TestOne('test_one')
suite.addTest(case1)
# 方法2 通过列表，将多个TestCase加入到TestSuite
cases_list = [TestOne('test_two'),TestIndex('test_index')]
suite.addTests(cases_list)
# 方法3 通过对象加载
suite.addTest(loader.loadTestsFromTestCase(TestLogin))

# text格式报告
# runner=unittest.TextTestRunner(verbosity=2)
# runner.run(suite)

# HTML报告

runner = HTMLTestRunner(stream=open("report.html", "wb"),  # 打开一个报告文件
                        description="接口测试报告",         # 报告中显示的描述信息
                        title="接口测试报告")            # 报告中网页现实的title
runner.run(suite)