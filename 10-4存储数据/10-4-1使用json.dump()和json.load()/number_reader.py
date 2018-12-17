import json
filename = 'numbers.json'
with open(filename) as f_obj:
    #使用函数json.load加载存储在numbers.json中的信息
    numbers = json.load(f_obj)
print(numbers)
#这是一种在程序之间共享数据的简单方式