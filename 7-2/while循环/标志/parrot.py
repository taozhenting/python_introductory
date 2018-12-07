prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
#设置一个标志，判断程序是否运行
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

