filename = 'guest.txt'
with open(filename,'w') as file_object:
    name = input("请输入您的姓名:")
    file_object.write(name)