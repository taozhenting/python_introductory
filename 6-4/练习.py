#将人物信息作为三个字典，然后放入peoples列表，全部打印出来
tao = {'first_name':'tao','last_name':'zhenting','age':'36','city':'Shanghai'}
wei = {'first_name':'wei','last_name':'yun','age':'32','city':'Shanghai'}
yuan = {'first_name':'tao','last_name':'siyuan','age':'1','city':'Shanghai'}
peoples = [tao,wei,yuan]
for people in peoples:
    print(people)

mimi = {'cat':'weiyun'}
wangwang = {'dog':'taozhenting'}
pets = [mimi,wangwang]
for pet in pets:
    print(pets)

favorite_places = {
    'tao':['japan','america','iceland'],
    'wei':['japan'],
    'yu':['japan','china'],
}

for name,places in favorite_places.items():
    print(
        name +
        "喜欢的地方是:"
    )
    for place in places:
        print(place)

numbers = {
    'tom':['3','6','8'],
    'alex':'5',
    'eric':['2','7'],
    'danile':['10','12'],
    'joan':'12',
}

for name,number in numbers.items():
    print(
        name +
        "喜欢的数字是:"
    )
    for nu in number:
        print(nu)