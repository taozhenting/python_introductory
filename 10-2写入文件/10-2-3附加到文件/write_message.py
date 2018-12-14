#如果要文件添加内容而不是覆盖，可以用附加模式
#写入到文件的行添加到文件末尾
#如果文件不存在，会自动创建文件
filename = 'programming.txt'
with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")