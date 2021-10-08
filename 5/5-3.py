#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   5-3.py
@Time    :   2021/10/08 17:04:51
@Author  :   CrissChan 
@Version :   1.0
@Site    :   https://blog.csdn.net/crisschan
@Desc    :   None
'''

host = 'http://127.0.0.1:50051'# 服务端地址和端口号
try:# 服务端地址和端口号
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='criss'))
        print(response)
except (KeyboardInterrupt, SystemExit):
    sys.exit(0)
