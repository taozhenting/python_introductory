sandwich_orders = ['五香烟熏牛肉三明治','鸡肉三明治','五香烟熏牛肉三明治','金枪鱼三明治','牛肉三明治','五香烟熏牛肉三明治',]
finished_sandwiches = []
print('五香烟熏牛肉三明治卖完了.')
while '五香烟熏牛肉三明治' in sandwich_orders:
    sandwich_orders.remove('五香烟熏牛肉三明治')
while sandwich_orders:
    sanwich = sandwich_orders.pop()
    print(
        "我帮你制作好三明治:" +
        sanwich +
        "."
    )
    finished_sandwiches.append(sanwich)
print("三明治列表:")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)