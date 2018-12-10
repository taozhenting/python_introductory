#披萨配料
while True:
    message = input("请输入披萨配料:")
    if message == 'quit':
        break
    else:
        print(
            "我们会在披萨中添加这种配料:" +
            message +
            "."
        )