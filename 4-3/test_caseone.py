#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   test_1.py
@Time    :   2021/09/29 10:19:29
@Author  :   CrissChan 
@Version :   1.0
@Site    :   https://blog.csdn.net/crisschan
@Desc    :   unittest Test Fixture 
'''
from unittest import TestCase, main
import unittest


class TestOne(TestCase):
    def setUp(self) -> None:
        print('TestCase {} ready for running'.format(self))
        return super().setUp()
    def tearDown(self) -> None:
        print('TestCase {} ready for stopping'.format(self))
        return super().tearDown()
    def test_one(self):
        print('test_one is run')
    def test_two(self):
        print('test_two is run')
