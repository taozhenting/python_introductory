#T恤
def make_shirt(chicun,ziyang):
    print(
        "衣服尺寸:" +
        chicun +
        "."
    )
    print(
        "衣服字样:" +
        ziyang +
        "."
    )

#位置实参
make_shirt("170","魔兽世界")

#关键字实参
make_shirt(ziyang="魔兽世界",chicun="180")