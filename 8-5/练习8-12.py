def make_sanwich(*toppings):
    print("\n您的三明治食材:")
    for topping in toppings:
        print(topping)

make_sanwich('番茄','鸡蛋')
make_sanwich('番茄','鸡蛋','叉烧')
make_sanwich('番茄','鸡蛋','牛肉')