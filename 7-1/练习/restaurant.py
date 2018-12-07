#餐馆订位
number = input("请问多少人用餐?")
number = int(number)
if number <= 8:
    print("有空桌")
else:
    print("没空桌")