from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
#OrderedDict类作用是根据添加顺序排序
for name,language in favorite_languages.items():
    print(
        name.title() +
        "'s favorite language is " +
        language.title() +
        "."
    )