#打开文件并访问
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    #最后一行会多出个空行，如何删除空行，详见file_reader2.py
    print(contents)