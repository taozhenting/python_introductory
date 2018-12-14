#这个程序没有采取任何处理错误的措施，因此让它执行除数0会崩溃
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    answer = int(first_number)/int(second_number)
    print(answer)
#程序崩溃可不好，让用户看到traceback不是好主意。
#不懂技术的人会被它们搞糊涂。
#懂技术的人可能会根据错误拿取隐私信息，对你代码进行攻击。