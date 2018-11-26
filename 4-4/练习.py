my_foods=['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
#使用切片打印前三个
print('The first three items in the list are:')
for my_food in my_foods[:3]:
    print(my_food)

#使用切片打印中间三个
print('Three items from the middle of the list are:')
for my_food in my_foods[1:4]:
    print(my_food)

#使用切片打印末尾三个
print('The last three items in the list are:')
for my_food in my_foods[-3:]:
    print(my_food)

#复制列表
friend_foods=my_foods[:]
my_foods.append('apple')
friend_foods.append('milk')
#打印列表
print('My favorite foods are:')
for my_food in my_foods:
    print(my_food)

print("My friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food)