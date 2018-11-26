cars=['audi','bmw','subaru','toyota']
#判断bmw就大写，其他首字母大写
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

