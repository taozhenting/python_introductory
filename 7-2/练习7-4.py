#披萨配料
active = True
while active:
    message = input("请输入披萨配料:")
    if message == 'quit':
        active = False
    else:
        print(
            "我们会在披萨中添加这种配料:" +
            message +
            "."
        )