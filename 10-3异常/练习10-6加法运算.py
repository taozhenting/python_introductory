print("请输入两个数字，它们会进行相加")
number1 = input("请输入数字1:")
number2 = input("请输入数字2:")
try:
    total = int(number1) + int(number2)
    print(total)
except ValueError:
    print("您输入的不是数字！")