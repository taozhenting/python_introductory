import json
numbers = [2,3,5,7,11,13]
filename = 'numbers.json'
with open(filename,'w') as f_obj:
    #函数json.dump()将数字列表存储到文件numbers.json中
    json.dump(numbers,f_obj)