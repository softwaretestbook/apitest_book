#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   index_stress.py
@Time    :   2021/10/20 17:28:18
@Author  :   CrissChan 
@Version :   1.0
@Site    :   https://blog.csdn.net/crisschan
@Desc    :   locust  script 有执行顺序
'''


#引入Locust的httplocust、Taskset和task
from locust import HttpUser, SequentialTaskSet, task


#定义用户行为也就是测试用例
class IndexTask(SequentialTaskSet):
    '''
    the VUser' behavior
    '''
    @task
    def index(self):
        self.client.get('/')# 访问主页

    @task
    def index1(self):
        self.client.get('/')# 访问主页

# 设置测试场景
class WebsiteUser(HttpUser):
    tasks = [IndexTask]# 将测试用例加入到测试任务套件中
    min_wait = 1# 每个请求间最小等待时间
    max_wait = 5 # 每个请求间最大等待时间
    host = 'http://127.0.0.1:12356'
    weight=1#每一个HttpUser场景别运行的权重，数值越大表示被执行的比例越大。

# 设置测试场景
class WebsiteAdmin(HttpUser):
    tasks = [IndexTask]#将测试用例加入到测试任务套件中
    min_wait = 1# 每个请求间最小等待时间
    max_wait = 5 # 每个请求间最大等待时间
    host = 'http://127.0.0.1:12356'
    weight=2 #每一个HttpUser场景别运行的权重，数值越大表示被执行的比例越大。
