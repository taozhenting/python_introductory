#增加用户验证，错误的话让用户输入正确用户名
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
        tmpname = input("请输入您的用户名进行验证:")
        if username == tmpname:
            print(
                "Welcom back, " +
                username +
                "!"
            )
        else:
            get_new_username()
    else:
        username = get_new_username()
        print(
            "We'll remember you when you come back, " +
            username +
            "!"
        )

greet_user()