#通过相对路径访问文件
#注意linux是 / 斜杠，windows是 \ 斜杠
with open('text_files\pi_digits.txt') as file_object:
    contents = file_object.read()
    # rstrip()方法删除空行
    print(contents.strip())