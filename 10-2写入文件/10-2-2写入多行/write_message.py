filename = 'programming.txt'
with open(filename,'w') as file_object:
    #末尾需要加换行符
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
