#重构greet_user(),让它不执行这么多任务，将存储用户名的代码移到另一个函数。
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
        username = input("What is your name?")
        filename = 'username.json'
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            print(
                "We'll remember you when you come back, " +
                username +
                "!"
            )

greet_user()