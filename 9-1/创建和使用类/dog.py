#创建小狗的类
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        """初始化属性name和age
        通过实例访问的变量成为属性
        """
        self.name = name
        self.age = age
    def site(self):
        """模拟小狗被命令时蹲下"""
        print(
            self.name.title() +
            " is now sitting."
        )
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(
            self.name.title() +
            " rolled over!"
        )

#根据类创建实例
#我们通常认为字母大写的名称（Dog）指的是类
#而小写名称（my_dog）指的是根据类创建的实例
my_dog = Dog('willie',6)

#访问实例
#可使用句点表示法。
#my_dog.name
print(
    "My dog's name is " +
    my_dog.name.title() +
    "."
)
print(
    "My dog is " +
    str(my_dog.age) +
    " years old."
)

#调用方法
#可以使用句点表示法调用Dog类中定义的任何方法。
my_dog = Dog('willie',6)
my_dog.site()
my_dog.roll_over()

#创建多个实例
#可以根据类创建任意数量的实例
my_dog = Dog('willie',6)
your_dog = Dog('lucy',3)
print(
    "My dog's name is " +
    my_dog.name.title() +
    "."
)
print(
    "My dog is " +
    str(my_dog.age) +
    " years old."
)
my_dog.site()
print(
    "\nYour dog's name is " +
    your_dog.name.title() +
    "."
)
print(
    "Your dog is " +
    str(your_dog.age) +
    " years old."
)
your_dog.site()