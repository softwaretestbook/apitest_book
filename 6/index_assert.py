#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   index_assert.py
@Time    :   2021/10/21 17:10:41
@Author  :   CrissChan 
@Version :   1.0
@Site    :   https://blog.csdn.net/crisschan
@Desc    :   None
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
      with self.client.get('/', catch_response=True) as response:  # 访问首页，通过catch_response = True设定该请求被标记为失败。
            if response.staus_code == 404:  # 判断如果是404的状态码就报告这次的请求失败
                response.faile('index is error')


# 设置测试场景
class WebsiteUser(HttpUser):
    tasks = [IndexTask]# 将测试用例加入到测试任务套件中
    min_wait = 1# 每个请求间最小等待时间
    max_wait = 5 # 每个请求间最大等待时间
    host = 'http://127.0.0.1:12356'
    weight=1#每一个HttpUser场景别运行的权重，数值越大表示被执行的比例越大。

