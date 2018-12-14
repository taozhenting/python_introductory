file_name = 'pi_million_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
#创建变量存储值
pi_string = ''
#循环将各行加入pi_string，并删除末尾的换行符。
for line in lines:
    #删除行和空格使用strip()
    pi_string += line.strip()
print(pi_string[:52] + "...")
print(len(pi_string))