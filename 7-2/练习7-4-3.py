#披萨配料
message=""
while message != 'quit':
    message = input("请输入披萨配料:")
    if message != 'quit':
        print(
            "我们会在披萨中添加这种配料:" +
            message +
            "."
        )