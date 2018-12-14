def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry,the file " + filename + "does not exsit."
        print(msg)
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
#循环读取书本，就算找不到书，也会继续运行，并且打印相应报错
for filename in filenames:
        count_words(filename)