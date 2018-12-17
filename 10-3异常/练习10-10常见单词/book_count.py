filename = "pg58473.txt"
with open(filename) as file_name:
    contents = file_name.read()
    #不区分大小写
    num = contents.lower().count('the')
    print(
        "在 " +
        filename +
        " the 出现了" +
        str(num) +
        "次。"
    )