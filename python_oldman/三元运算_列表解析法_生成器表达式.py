#!/usr/bin/python
# -*- coding: utf-8 -*-

egg_list = []
for i in range(10):
    egg_list.append('鸡蛋 %s' %i)
print(egg_list)

#列表解析法
l = [ i for i in range(10) ]
print(l)
l1 = [ '鸡蛋 %s' %i for i in range(10) ]
print(l1)
l2 = [ '鸡蛋 %s' %i for i in range(10) if i > 5 ]
print(l2)
#最多三元表达式，没有四元表达式
# l3 = [ '鸡蛋 %s' %i for i in range(10) if i > 5 else i ]

#生成器表达式
laomuji = ( '鸡蛋 %s' %i for i in range(10) )
print(laomuji)
print(laomuji.__next__())
print(laomuji.__next__())
print(next(laomuji))