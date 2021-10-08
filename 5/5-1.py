#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   5-1.py
@Time    :   2021/10/08 13:29:56
@Author  :   CrissChan 
@Version :   1.0
@Site    :   https://blog.csdn.net/crisschan
@Desc    :   None
'''

import json

from common import Common
res= '{"result":0,"data":[{"word":"\u6027\u80fd\u6d4b\u8bd5"},{"word":"\u6027\u80fd"},{"word":"\u6027\u80fd\u4f18\u5316"},{"word":"\u6027\u80fdce"},{"word":"\u6027\u80fdc"}],"msg":"\u6210\u529f"}'
print('反序列化：')
dict = json.loads(res)
print(dict)#打印反序列化的dict
print(type(dict))#打印dict的类型
print('序列化：')
ser=json.dumps(dict)
print(ser)#打印序列化的ser
print(type(ser))#打印ser的类型

# 建立和WebSocket接口的链接
con = Common('ws://echo.websocket.org','ws')
# 获取返回结果
result = con.send('Hello, World...')
#打印日志
print(result)
#释放WebSocket的长连接
del con