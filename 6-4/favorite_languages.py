#字典里面套列表
favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}

for name,languages in favorite_languages.items():
    print("\n" +
          name.title() +
          "'s favorite languages are:")
    for language in languages:
        print("\t" +
              language.title())
print(
    "\n-------------------------\n"
)
#增加if判断，单个编程打印另外一句
for name,languages in favorite_languages.items():
    if len(languages) == 1:
        for language in languages:
            print("\n" +
                name.title() +
                "'s favorite languages is: " +
                  language.title())
    else:
        print("\n" +
              name.title() +
              "'s favorite languages are:")
        for language in languages:
            print("\t" +
                    language.title())

