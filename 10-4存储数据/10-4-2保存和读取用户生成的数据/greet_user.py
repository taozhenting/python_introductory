import json
filename = 'username.json'
#读取文件的用户名
with open(filename) as f_obj:
    username = json.load(f_obj)
    print(
        "Welcom back, " +
        username +
        "!"
    )