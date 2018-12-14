#逐行读取文件
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        #这样打印，空行就更多了。
        #因为在每行末尾有一个看不见的换行符。
        #去除空行，详见file_reader2.py
        print(line)