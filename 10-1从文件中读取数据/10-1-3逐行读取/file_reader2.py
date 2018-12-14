#逐行读取文件,并删除空行
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        #rstrip()方法删除空行
        print(line.rstrip())