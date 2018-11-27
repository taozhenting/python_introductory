#4岁以下免费
#4~8岁收费5美元
#18岁（含）以上收费10美元
age = 12
if age < 4:
    print("Your admission cost is $0 .")
elif age < 18:
    print("Your admission cost is $5 .")
else:
    print("Your admission cost is $10 .")

#简洁代码写法：
age =12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

#追加对于65岁（含）以上的老人，可以半价（即5美元）购买门票：
age =12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")

#省略else代码块
age =12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")