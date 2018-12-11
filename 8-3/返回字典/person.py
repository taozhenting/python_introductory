def build_person(first_name,last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {
        'first':first_name,
        'last':last_name
    }
    return person
musician = build_person('jimi','hendrix')
print(musician)

#增加可选参数age
def build_person(first_name,last_name,age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {
        'first': first_name,
        'last': last_name
    }
    if age:
        person['age'] = age
    return person
musician = build_person('jimi','hendrix',age=27)
print(musician)

