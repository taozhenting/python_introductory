"""一组可用于表示电动汽车的类"""
from car import Car
class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    #形参battery_size可选，默认值70
    def __init__(self,battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(
            "This car has a " +
            str(self.battery_size) +
            "-kWh battery."
        )
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range =270
        message = "This car can go approximately " + str(range)
        message += "miles on a full charge"
        print(message)
    def upgrade_battery(self):
        """检查电瓶容量，不是85将设置85"""
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        """
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make,model,year)
        #Battery是实例，该实例存储在属性self.battery中
        self.battery = Battery()