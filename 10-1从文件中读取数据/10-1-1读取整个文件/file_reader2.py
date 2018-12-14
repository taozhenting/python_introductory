#打开文件并访问,删除最后的空行
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    contents = file_object.read()
    #rstrip()方法删除空行
    print(contents.rstrip())