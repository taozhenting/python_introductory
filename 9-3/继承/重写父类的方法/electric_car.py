class Car():
    """增加行里程初始值"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        #属性设置了初始值，就不用设置形参
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print(
            "This car has " +
            str(self.odometer_reading) +
            " miles on it."
        )
    def update_odometer(self,mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
    #新增一个油箱的方法
    def fill_gas_tank(self):
        print(
            "This Car needs a gas tank!"
        )

#创建子类
class ElectricCar(Car):
    """电动汽车的独特之处"""
    #方法__init__()让子类包含父类的所有属性
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        #super()是一个特殊函数，帮助python将父类和子类关联起来
        #调用了父类的方法__init__()，让子类包含父类的所有属性，父类也称为超类。
        super().__init__(make,model,year)
    #对父类的fill_gas_tank方法进行重写
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This Car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla','model s','2016')
my_tesla.fill_gas_tank()