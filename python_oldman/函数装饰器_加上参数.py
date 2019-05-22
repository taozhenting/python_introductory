#!/usr/bin/python
# -*- coding: utf-8 -*-

def auth_func(func):
    def wrapper(*args,**kwargs):
        username = input('用户名： ').strip()
        passwd = input('密码： ').strip()
        if username == 'sb' and passwd == '123':
            res = func(*args,**kwargs)
            return res
        else:
            print('用户名或密码错误')
    return wrapper

@auth_func
def index():
    print('欢迎来到京东主页')

@auth_func
def home(name):
    print('欢迎回家, %s' %name)

@auth_func
def shopping_car(name):
    print('%s购物车里有[%s,%s,%s]' %(name,'奶茶','妹妹','娃娃'))

index()
home('产品经理')
shopping_car('产品经理')