filename = 'guest.txt'
with open(filename, 'w') as file_object:
    while True:
        with open(filename, 'a') as file_object:
            print("输入quit退出")
            name = input("请输入您的姓名:")
            if name == 'quit':
                break
            else:
                print(
                    "Hello, " +
                    name +
                    "!\n"
                )
                file_object.write(
                    "Hello, " +
                    name +
                    "!\n"
                )
