users=['admin','tom','eric','alex','max']
users=[]

#判断用户列表是否为空，判断admin用户并打印
if users:
    for user in users:
        if user == 'admin':
            print("Hello " + user + ",would you like to see a status report?")
        else:
            print("Hello " + user + ",thank you for logging in again.")
else:
    print("We need to find some users!")

#比较用户名，并不区分大小写
current_users=['aDmin','tom','eric','alex','max']
new_users=['Admin','eileen','eric','daniel','joan']
current_users_lower=[]
for current_user in current_users:
    current_users_lower.append(current_user.lower())
print(current_users_lower)
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(new_user + "用户名已存在")
    else:
        print(new_user + "用户名未被使用")

#列表解析写法
current_users=['aDmin','tom','eric','alex','max']
new_users=['Admin','eileen','eric','daniel','joan']
for new_user in new_users:
    if new_user.lower() in [current_user.lower() for current_user in current_users]:
        print(new_user + "用户名已存在")
    else:
        print(new_user + "用户名未被使用")

numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    print(number)

for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")