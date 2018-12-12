#创建类
class Restaurant():
    """餐馆名字和类型"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(
            "\n餐馆的名字是" +
            self.restaurant_name +
            "."
        )
        print(
            "餐馆的类型是" +
            self.cuisine_type +
            "."
        )
    def open_restaurant(self):
        print(
            self.restaurant_name.title() +
            "正在营业!"
        )

#三家餐馆
bishengke = Restaurant('必胜客','西餐')
xialiya = Restaurant('夏丽雅','新疆餐')
xiaonanguo = Restaurant('小南国','中餐')

bishengke.describe_restaurant()
xialiya.describe_restaurant()
xiaonanguo.describe_restaurant()