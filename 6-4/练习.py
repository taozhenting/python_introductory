#将人物信息作为三个字典，然后放入peoples列表，全部打印出来
tao = {'first_name':'tao','last_name':'zhenting','age':'36','city':'Shanghai'}
wei = {'first_name':'wei','last_name':'yun','age':'32','city':'Shanghai'}
yuan = {'first_name':'tao','last_name':'siyuan','age':'1','city':'Shanghai'}
peoples = [tao,wei,yuan]
for people in peoples:
    print(people)

#宠物
mimi = {'cat':'weiyun'}
wangwang = {'dog':'taozhenting'}
pets = [mimi,wangwang]
for pet in pets:
    print(pets)

#喜欢的地方
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

#喜欢的数字
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

#城市
cities = {
    '上海':{
        'country':'中国',
        'population':'2000万',
        'fact':'商业城市'
    },
    '札幌':{
        'country':'日本',
        'population':'194万',
        'fact':'旅游城市'
    },
    '北京':{
        'country':'中国',
        'population':'2170万',
        'fact':'行政城市'
    }
}

for name,city_info in cities.items():
    print(
        name +
        "的国家:" +
        city_info['country'] +
        ", 人口:" +
        city_info['population'] +
        ", 属于:" +
        city_info['fact'] +
        "."
    )

#扩展
cities['香港'] = {
    'country':'中国',
    'population':'740万',
    'fact':'自由城市'
}

for name,city_info in cities.items():
    print(
        name +
        "的国家:" +
        city_info['country'] +
        ", 人口:" +
        city_info['population'] +
        ", 属于:" +
        city_info['fact'] +
        "."
    )