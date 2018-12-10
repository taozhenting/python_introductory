#电影票价，不到3岁免费，3到12岁10美元，超过12岁15美元
prompt = "请输入您的年龄:"
while True:
    age = input(prompt)
    age = int(age)
    if age < 3:
        print("您的电影票价免费!")
        break
    elif age <= 12:
        print("您的电影票价10美元!")
        break
    else:
        print("您的电影票价15美元!")
        break
