#打印奇数，continue跳回循环开头，忽略下面代码。偶数被2整除，忽略打印。
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)