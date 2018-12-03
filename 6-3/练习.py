#词汇表2
pythons = {
    'if':'判断',
    'for':'循环',
    'print':'打印',
    'del':'删除',
    'append':'追加',
    'title':'首字母大写',
    'keys':'键',
    'values':'值',
    'set':'集合',
    'items':'键和值'
}

for name,python in pythons.items():
    print(name +
          ":\n" +
          "\t" +
          python)

#三大河流
rivers = {
    'yangtze':'china',
    'mississippi':'america',
    'nile':'egypt'
}

for river,country in rivers.items():
    print(
        "The " +
        river.title() +
        "runs through " +
        country.title() +
        "."
    )

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)

#已检查调查人员
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

personnel_list = ['jen','sarah','edward','tom','phil']

for personnel in personnel_list:
    if personnel not in favorite_languages.keys():
        print(
            "Hi " +
            personnel +
            " 邀请您进行调查！"
        )
    else:
        print(
            "感谢" +
            personnel +
            "接受调查！"
        )

