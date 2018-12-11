#位置实参就是按照顺序排序的实参
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print(
        "\nI have a " +
        animal_type +
        "."
    )
    print(
        "My " +
        animal_type +
        "'s name is " +
        pet_name.title() +
        "."
    )

describe_pet('hamster','harry')
describe_pet('dog','willie')
#位置实参顺序很重要，如果写反，结果会出乎意料
describe_pet('harry','hamster')