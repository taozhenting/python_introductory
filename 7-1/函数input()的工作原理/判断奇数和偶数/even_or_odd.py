number = input("Enter a number, and I'll tell you if it's even or odd:")
number = int(number)
# %求余数，偶数是0，其他是奇数
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")