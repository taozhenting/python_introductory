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

#创建restaurant实例
restaurant = Restaurant('必胜客','西餐')
#打印restaurant_name属性
print(restaurant.restaurant_name)
#打印cuisine_type属性
print(restaurant.cuisine_type)
#调用describe_restaurant方法
restaurant.describe_restaurant()
#调用open_restaurant方法
restaurant.open_restaurant()