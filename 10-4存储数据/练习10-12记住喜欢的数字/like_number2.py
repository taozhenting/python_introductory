#如果存储了用户喜欢的数字就显示它，否则提示输入喜欢的数字并存储文件
import json
filename = 'number.json'
try:
    with open(filename) as f_obj:
        number = json.load(f_obj)
except FileNotFoundError:
    number = input("请输入您喜欢的数字?")
    with open(filename,'w') as f_obj:
        json.dump(number,f_obj)
    print(
        "I know your favorite number!It's " +
        number +
        "."
    )
else:
    print(
        "I know your favorite number!It's " +
        number +
        "."
    )