#将错误代码放入try代码块
#如果try代码块中的代码没问题，将会跳过except代码块
#如果try代码块中的代码有问题，就会查找except代码块，并运行其中的代码，如果后面还有代码会继续运行
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide zero!")