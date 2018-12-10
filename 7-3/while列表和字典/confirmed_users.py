#首先创建一个待验证用户列表
unconfirmed_users = ['alice','brian','candace']
#和一个用于存储已验证用户的空列表
confirmed_users = []

#unconfirmed_users列表为空退出循环
while unconfirmed_users:
    #从列表尾部开始删除用户，并加入current_user变量
    #pop方法默认删除尾部最后一个，并可以使用它。类似弹出一个值，也可以pop(0)指定列表某个值。
    current_user = unconfirmed_users.pop()
    print(
        "Verifying user:" +
        current_user.title()
    )
    #验证用户列表加入这个用户
    confirmed_users.append(current_user)
    print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
print(unconfirmed_users)

