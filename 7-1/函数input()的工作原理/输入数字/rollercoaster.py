#判断一个人是否满足坐过山车的身高要求
height = input("How tall are you, in inches?")
#将字符串转换为数字
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")