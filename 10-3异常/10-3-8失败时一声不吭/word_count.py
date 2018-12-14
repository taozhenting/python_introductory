def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        #当发生错误什么都不做
        pass
    else:
        # 计算文件大致包含多少个单词
        # split()方法以空格为分隔符将字符串拆分多个部分，并存到一个列表中
        words = contents.split()
        num_words = len(words)
        print(
            "The file " +
            filename +
            " has about " +
            str(num_words) +
            " words."
        )

filenames = ['alice.txt','siddhartha.txt','moby_dict.txt','little_women.txt']
#这次报错什么都不显示，只显示正确信息
#我们可以将找不到书放到missing_file.txt中，用户看不到这个文件，但我们可以读取这个文件。
for filename in filenames:
        count_words(filename)