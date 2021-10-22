#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   baidu_param.py
@Time    :   2021/10/21 17:16:13
@Author  :   CrissChan 
@Version :   1.0
@Site    :   https://blog.csdn.net/crisschan
@Desc    :   locust 参数化设置
'''


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/19 2:51 PM
# @Author  : Criss Chan
# @Site    : 
# @File    : load_test.py
# @Software: PyCharm
# @instruction：locust baidu script

# 引入Locust的httplocust、Taskset和task
from locust import HttpUser, TaskSet, task
from random import randint


# 定义用户行为也就是测试用例
class BaiDuSearch(TaskSet):
    '''
    the VUser' behavior
    '''

    @task
    def baidu_search(self):

     
        keyword=['接口测试','UI测试']# 搜索关键字

        param_index = randint(0,1)#生成一个0到1的在整形随机值
        search_uri = '/s?wd='+keyword[param_index]#拼接url


        with self.client.get(search_uri, catch_response=True) as response:#访问搜索
            if response.status_code == 200:#如果返回状态码是200，
                print(response.content)  # 打印返回的内容
                response.success()# 标记访问成功
            else:
                response.faile('search is error！')#否则标记访问失败



# 设置测试场景
class SearUser(HttpUser):
    tasks = [BaiDuSearch]
    min_wait = 1000
    max_wait = 3000
    host = "https://www.baidu.com"
