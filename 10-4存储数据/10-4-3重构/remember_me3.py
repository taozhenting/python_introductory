#将greet_user()中的另一个代码块取出来，将没有存储用户名时提示用户输入代码块放到一个独立函数
import json
def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        #返回None,可以通过函数返回值做简单判断
        return None
    else:
        #返回值
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print(
            "Welcom back, " +
            username +
            "!"
        )
    else:
        username = get_new_username()
        print(
            "We'll remember you when you come back, " +
            username +
            "!"
        )

greet_user()