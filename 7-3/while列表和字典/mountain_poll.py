responses = {}
#设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
    name = input("\n请输入您的姓名?")
    response = input("您要攀登哪座山?")
    #将答案存储在字典中
    responses[name] = response
    #看看是否还有人要参与调查
    repeat = input("是否还要继续调查?(yes/no)")
    if repeat == 'no':
        polling_active = False
#调查结束，显示结果
print("\n-------调查结果--------")
for name,response in responses.items():
    print(
        name +
        "想攀登" +
        response +
        "."
    )