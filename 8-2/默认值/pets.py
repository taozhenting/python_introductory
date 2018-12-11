#默认值是给形参指定实参，如果后续不定义，就使用默认实参
#在形参列表中必须先列出没有默认值的参数
def describe_pet(pet_name,animal_type='dog'):
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

describe_pet(pet_name='willie')
#注意默认值还是使用了位置实参，由于默认值已经有参数，所以排在后面,
describe_pet('willie')
describe_pet('willie','hamster')
describe_pet(pet_name='harry',animal_type='hamster')