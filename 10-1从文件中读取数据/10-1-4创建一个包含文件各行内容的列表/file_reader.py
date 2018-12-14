#将各行存储在一个列表中，再with代码块外打印它们。
filename = 'pi_digits.txt'
with open(filename) as file_object:
    #readlines方法从文件中读取每一行，并存储在一个列表下，然后列表存储在lines变量
    lines = file_object.readlines()
#在with代码块外，我们依然可以使用这个变量
for line in lines:
    print(line.rstrip())
    