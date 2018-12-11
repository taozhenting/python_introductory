#增加函数参数
#username是变量，在函数定义中叫形参
def greet_user(username):
    #文档字符串的注释，描述函数是做什么的
    """显示简单的问候句"""
    print(
        "Hello, " +
        username.title() +
        "!"
    )
#jesse值，在函数定义中叫实参
greet_user('jesse')
greet_user('sarah')