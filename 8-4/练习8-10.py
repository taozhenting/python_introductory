#了不起的魔术师名字列表
def make_great(names,great_names):
    while names:
        current_name = names.pop()
        great_name = "the Great " + current_name
        great_names.append(great_name)

def show_magicians(great_names):
    make_great(usernames, great_names)
    for name in great_names:
        print(
            "了不起的魔术师名字:" +
            name
        )
usernames = ['tao','wei','tom']
great_names = []
show_magicians(great_names)