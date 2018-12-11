#任意数量形参放在最后，python先匹配位置实参和关键字实参
#增加披萨尺寸
def make_pizza(size,*toppings):
    """概述要制作的披萨"""
    print(
        "\nMaking a " +
        str(size) +
        "-inch pizza with the following toppings:"
    )
    for topping in toppings:
        print("- " + topping)

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')