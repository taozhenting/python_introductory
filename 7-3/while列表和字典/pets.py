pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
#判断pets列表中是否有cat值
while 'cat' in pets:
    #remove会匹配第一个值cat进行删除，其他cat会在下次循环删除。
    pets.remove('cat')
    print(pets)