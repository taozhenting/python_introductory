car = 'subaru'
if car == 'subaru':
    print("ls car == 'subaru'? I predict True.")

if car != 'audi':
    print("ls car == 'audi'? I property False.")

car = 'Subaru'
if car.lower() == 'subaru':
    print("ls car == 'subaru'? I predict True.")

number=10
if number == 10:
    print('数字相等')

if number != 9:
    print('数字不等')

if number > 9:
    print('数字大于')

if number < 11:
    print('数字小于')

if number <= 10:
    print('数字大于等于')

if number >= 10:
    print('数字小于等于')

if number > 9 and number < 11:
    print('and测试')

if number > 9 or number < 8:
    print('or测试')

numbers=[1,2,3]
number=2
if number in numbers:
    print('in测试')

number=4
if number not in numbers:
    print('not in 测试')