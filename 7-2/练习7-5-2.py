#电影票价，不到3岁免费，3到12岁10美元，超过12岁15美元
prompt = "请输入您的年龄:"
active = True
while active:
    age = input(prompt)
    age = int(age)
    if age < 3:
        print("您的电影票价免费!")
        active = False
    elif age <= 12:
        print("您的电影票价10美元!")
        active = False
    else:
        print("您的电影票价15美元!")
        active = False