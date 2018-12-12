#增加禁止将里程表读数往回调
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

my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())
#通过方法修改
my_new_car.update_odometer(23)
my_new_car.read_odometer()
#小于里程表不允许修改
my_new_car.update_odometer(20)
my_new_car.read_odometer()