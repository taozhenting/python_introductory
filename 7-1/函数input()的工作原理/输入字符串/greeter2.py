#创建多行字符串的方式，变量传递给input()函数
prompt = "If you tell us who you are,we can personalize the messages you see."
#运算符+=在存储prompt中的字符串追加字符串
prompt += "\nWhat is your first name?"
name = input(prompt)
print(
    "\nHello, " +
    name +
    "!"
)
