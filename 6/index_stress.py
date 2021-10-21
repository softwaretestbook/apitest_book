#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   index_stress.py
@Time    :   2021/10/20 17:28:18
@Author  :   CrissChan 
@Version :   1.0
@Site    :   https://blog.csdn.net/crisschan
@Desc    :   locust  script
'''


#引入Locust的httplocust、Taskset和task
from locust import HttpUser, TaskSet, task

#定义用户行为也就是测试用例
class IndexTask(TaskSet):
    '''
    the VUser' behavior
    '''
    @task(100)
    def index(self):
        self.client.get('/')# 访问主页


# 设置测试场景
class WebsiteUser(HttpUser):
    tasks = [IndexTask]
    min_wait = 1# 每个请求间最小等待时间
    max_wait = 5 # 每个请求间最大等待时间
    host = 'http://127.0.0.1:12356'


