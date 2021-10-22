#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   load_test_grpc.py
@Time    :   2021/10/21 17:54:07
@Author  :   CrissChan 
@Version :   1.0
@Site    :   https://blog.csdn.net/crisschan
@Desc    :   None
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 4:08 下午
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : load_test_grpc.py
# @Software: 这是调用gRPC的Locust脚本

import sys
import grpc
import inspect
import time
import gevent
from locust.contrib.fasthttp import FastHttpUser
from locust import task, events, constant
from locust.runners import STATE_STOPPING, STATE_STOPPED, STATE_CLEANUP, WorkerRunner
import helloworld_pb2
import helloworld_pb2_grpc

def stopwatch(func):
    
    def wrapper(*args, **kwargs):
       
       
        previous_frame = inspect.currentframe().f_back
        _, _, task_name, _, _ = inspect.getframeinfo(previous_frame)
        start = time.time()
        result = None
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            total = int((time.time() - start) * 1000)
            events.request_failure.fire(request_type="TYPE",
                                        name=task_name,
                                        response_time=total,
                                        response_length=0,
                                        exception=e)
        else:
            total = int((time.time() - start) * 1000)
            events.request_success.fire(request_type="TYPE",
                                        name=task_name,
                                        response_time=total,
                                        response_length=0)
        return result
    return wrapper

class GRPCMyLocust(FastHttpUser):
    host = 'http://127.0.0.1:50051'# 服务端地址和端口号
    wait_time = constant(0)
    def on_start(self):
        pass
    def on_stop(self):
        pass
    @task
    @stopwatch
    def grpc_client_task(self):
        try:# 服务端地址和端口号
            with grpc.insecure_channel('127.0.0.1:50051') as channel:
                stub = helloworld_pb2_grpc.GreeterStub(channel)
                response = stub.SayHello(helloworld_pb2.HelloRequest(name='criss'))
                print(response)
        except (KeyboardInterrupt, SystemExit):
            sys.exit(0)
