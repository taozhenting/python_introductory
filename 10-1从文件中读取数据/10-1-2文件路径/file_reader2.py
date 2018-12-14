#通过绝对路径访问文件
#注意linux是 / 斜杠，windows是 \ 斜杠
#注意在windows中确保万无一失，应以原始字符串方式知道路径，即在开头的单引号前加上r
file_path = r'C:\Users\taozhenting\PycharmProjects\python\10-1从文件中读取数据\10-1-2文件路径\text_files\pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    # rstrip()方法删除空行
    print(contents.strip())