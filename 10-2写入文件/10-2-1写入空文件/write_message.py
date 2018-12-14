filename = 'programming.txt'
#第二个实参w写入模式，r读取模式，a附加模式或是r+，就是读写兼备模式。
#如果你省略了模式实参，默认是只读模式。
#如果你写入的文件不存在，函数open()将自动创建它。
#写入模式w打开文件时千万小心，如果文件已存在，会清空该文件！
with open(filename,'w') as file_object:
    file_object.write("I love programming.")
#注意只能写入字符串文本，如果是数值，需要函数str()转换
