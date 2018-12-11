#关键字实参是参数和值一一对应，直接关键，所以无需考虑顺序
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

describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(pet_name='harry',animal_type='hamster')