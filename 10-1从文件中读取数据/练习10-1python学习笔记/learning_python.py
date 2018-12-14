#用三种方法读取打印文件
file_name = 'learning_python.txt'
with open(file_name) as file_object:
    #第一种方式，读取打印整个文件
    contents = file_object.read()
    print(contents.rstrip())

with open(file_name) as file_object:
    #第二种方式，读取打印遍历文件对象
    for line in file_object:
        print(line.rstrip())

with open(file_name) as file_object:
    #第三种方式，打印时将各行存储在一个列表中
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())