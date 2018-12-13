#创建类
class Restaurant():
    """餐馆名字和类型"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
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
    def read_number_served(self):
        if self.number_served > 60:
            print("警告:已超过餐馆最大人数60")
        print(
            self.restaurant_name.title() +
            "目前就餐人数:" +
            str(self.number_served) +
            "人。"
        )
    def set_number_served(self,served):
        self.number_served = served
    def increment_number_served(self,served):
        self.number_served += served

class IceCreamStand(Restaurant):
    """冰激凌小店"""
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors
    def read_icecreamstand(self):
        print(
            "\n冰激凌口味有:"
        )
        for self.flavor in self.flavors:
            print(self.flavor)

IceCreamStand = IceCreamStand('旋风桃子冰激凌','冰激凌小店',['草莓味','香草味','巧克力味'])
IceCreamStand.describe_restaurant()
IceCreamStand.read_icecreamstand()
IceCreamStand.increment_number_served(10)
IceCreamStand.read_number_served()