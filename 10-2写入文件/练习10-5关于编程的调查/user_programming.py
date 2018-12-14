#编程的调查，询问用户为何喜欢编程，输入后打印并写入文件。
filename = 'grogramming.txt'
#每次运行前清空文件，并写入模式
with open(filename, 'w',encoding='utf-8') as file_object:
    while True:
        #循环模式中使用添加模式
        with open(filename, 'a',encoding='utf-8') as file_object:
            print("输入quit退出")
            name = input("请输入您的姓名:")
            if name == 'quit':
                break
            print(
                "\nHello, " +
                name +
                "!"
            )
            file_object.write(
                "Hello, " +
                name +
                "!\n"
            )
            reason = input("请输入您编程的原因:")
            if reason == 'quit':
                break
            print(
                name +
                "编程的原因是:" +
                reason +
                "。\n"
            )
            file_object.write(
                name +
                "编程的原因是:" +
                reason +
                "。\n"
            )