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


#创建restaurant实例
restaurant = Restaurant('必胜客','西餐')
#调用describe_restaurant方法
restaurant.describe_restaurant()
#调用open_restaurant方法
restaurant.open_restaurant()
#直接修改number_sered属性的值（用餐人数）
restaurant.number_served=23
#调用read_number_served方法，查看多少人用餐
restaurant.read_number_served()
#通过set_number_served方法，设置就餐人数
restaurant.set_number_served(20)
#调用read_number_served方法，查看多少人用餐
restaurant.read_number_served()
#调用increment_number_served方法，递增就餐人数
restaurant.increment_number_served(50)
restaurant.read_number_served()
#餐厅最大人数60人，超过就会警告。