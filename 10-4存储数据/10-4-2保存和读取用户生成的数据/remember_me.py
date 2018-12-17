import json
username = input("What is your name?")
filename = 'username.json'
#将用户名存储到文件
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print(
        "We'll remember you when you come back, " +
        username +
        "!"
    )