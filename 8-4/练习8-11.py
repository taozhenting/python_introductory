#调用函数不修改原始列表，并且分别打印两个列表
def make_great(names,great_names):
    while names:
        current_name = names.pop()
        great_name = "the Great " + current_name
        great_names.append(great_name)

def show_magicians(great_names):
    #判断如果列表是空就执行
    if great_names:
        for name in great_names:
            print(
                "魔术师名字:" +
                name
            )
    else:
        make_great(usernames[:], great_names)
        for name in great_names:
            print(
                "了不起的魔术师名字:" +
                name
            )


usernames = ['tao','wei','tom']
great_names = []
show_magicians(usernames)
show_magicians(great_names)