favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
#遍历字典
for name,language in favorite_languages.items():
    print(name.title() + "'s favorite language is" +
          language.title() + ".")

#遍历字典中的所有键
for name in favorite_languages.keys():
    print(name.title())

#判断朋友并打印
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() +
              ",I see your favorite language is " +
              favorite_languages[name].title() + "!")

#判断某人是否接受调查
if 'erin' not in favorite_languages.keys():
    print("Erin,please take our poll!")

#字典的键排序
for name in sorted(favorite_languages.keys()):
    print(name.title() + ",thank you for taking the poll.")

#遍历字典中的所有值
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#剔除重复的值（set集合）
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

