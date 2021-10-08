#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/13 16:43
# @Author  : CrissChan
# @Site    : https://blog.csdn.net/crisschan
# @File    : 4.py
# @Software: PyCharm
#
# aparam = 10
# bparam = 'a'
# cparam = 10.4
# dparam = {'key':'value'}
# eparam = ['f',3]
# fparam = True
# type(aparam)
# type(bparam)
# type(cparam)
# type(dparam)
# type(eparam)
# type(fparam)
#
# 十进制
a = 10
print(a)
# 二进制
b = 0b10
print(b)
# 八进制
c = 0o10
print(c)
# 十六进制
d = 0x10
print(d)

e = 4e10
print(e)
f = 3.1415926
print(f)
print(bool(0))
print(bool(0.0))
print(bool(1))
print(bool(1.1))
print(bool(-1))
print(bool(-1.1))

a_str='criss is "boy"'
b_str="'criss' 'is' 'boy'"

print(a_str)
print(b_str)

a_mulistr='''criss
is the
boy'''

b_mulistr="""criss
is the
man"""

print(a_mulistr)
print(b_mulistr)

c_alinestr = 'criss is "the ' \
             'boy"'

print(c_alinestr)
print(a_str[6:8])
print(a_str[-2:])
# a_str[0]='a'

a_str='criss is '
b_str = 'the  boy.'
print(a_str+b_str)

a_funcstr = 'Informaiton'
alist = [1,2,3]
print(len(a_funcstr))
print(str(alist))


print(a_funcstr.upper())
print(a_funcstr.lower())

a_str = '    Informaiton'
a_str.strip()
a_str = '12334'
a_str.isdigit()
a_str = 'fsadfsaf'
a_str.isalpha()

a_str = 'this is a cat'
print(a_str.replace('cat','dog'))
print(a_str.split(' '))
print('-'.join(['this', 'is', 'a', 'cat']))
print(bool(''))
print(bool('3'))

a_list=[]
b_list=list()

a_list=['a','b',3,5]
b_list=['car','bus','train']
a_list[2] = '4'
print(a_list)

a_list=['a','b',3,5]
b_list=['car','bus','train']
a_list.append('criss')
print(a_list)

a_list.append(b_list)
print(a_list)

a_list.insert(0,'criss')
print(a_list)

print('##')

a_list=['a','b',3,5,3]
print(a_list.reverse())

a_list.remove(3)
print(a_list)
a_list.pop()
print(a_list)
a_list.pop(0)
print(a_list)
a_list=[1,4,6,3,4,2,6,8]
a_list.sort()
print(a_list)

#Tuple

a_tuple = ('car','plan','train')

print(a_tuple[0])
a_tuple = ('car','plan','train','bus','bike','walk')
print(a_tuple[0])
print(a_tuple[0:3])
print(a_tuple[-3:-1])

b_tuple = (1)
print(type(b_tuple))

b_tuple=(1,)
print(type(b_tuple))
b_tuple=(1,'2',[2,3,4])

b_tuple[2].append(5)
print(b_tuple)

a_tuple = ('car','airplan','train')
car,airplan,train = a_tuple
print(car)
print(airplan)
print(train)

a_tuple = ('car','airplan','train')
print('%s,%s,%s'%a_tuple)
_,_,train = a_tuple
print(train)
car,*other = a_tuple
print(car)
print(other)

a_set = {1,2,3,45}
for a_item in a_set:
    print(a_item)
b_set = set([1,2,3,4,5,6])
print(b_set)


a_set = {1,2,3,45}
b_set = set([1,2,3,4,5,6])
# 交集
print(a_set & b_set)
#并集
print(a_set | b_set)

a_set.add(1)
print(a_set)
a_set.remove(1)
print(a_set)
import copy
a_dict = {'name':'criss', 'age':'45', 'height':'170', 'weight':'70'}
b_dict =copy.deepcopy(a_dict)
b_dict['name']='chan'
print('a_dict:')
print(a_dict)
print('b_dict:')
print(b_dict)


a_list = [1,2,3,4,5]
b_list = copy.deepcopy(a_list)
b_list[0]=99
print('a_list:')
print(a_list)
print('b_list:')
print(b_list)

astr= 'aaaaaaa'
bstr=astr
bstr = bstr.replace('a','b')
print(astr)
print(bstr)

a_dict = {'name':'criss', 'age':'45', 'height':'170', 'weight':'70'}
a_dict['gender'] = 'male'
a_dict['weight'] = '60'
print(a_dict)

for key,value in a_dict.items():
    print('key:%s vaule:%s'%(key,value))
for akey in a_dict:
    print(akey)
    print(a_dict[akey])

for avalue in a_dict.values():
    print(avalue)
## None

print(None is {})
print(None is 0)
print(None is False)
print(None is [])
print(None is '')