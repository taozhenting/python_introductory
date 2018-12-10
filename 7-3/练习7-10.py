places = {}
polling_active = True
while polling_active:
    name = input("\n请输入您的姓名?")
    place = input("您喜欢哪个旅游胜地?")
    places[name] = place
    repeat = input("是否还要继续调查?(yes/no)")
    if repeat == 'no':
        polling_active = False
print("\n-------调查结果--------")
for name,place in places.items():
    print(
        name +
        "喜欢旅游胜地:" +
        place +
        "."
    )