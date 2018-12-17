#存储用户喜欢的数字，并打印消息
import json
def stored_number():
    """提示输入用户喜欢的数字，并存储文件"""
    number = input("请输入您喜欢的数字?")
    filename = 'number.json'
    with open(filename,'w') as f_obj:
        json.dump(number,f_obj)

def get_stored_number():
    stored_number()
    filename = 'number.json'
    with open(filename) as f_obj:
        number = json.load(f_obj)
    print(
        "I know your favorite number!It's " +
        number +
        "."
        )

get_stored_number()