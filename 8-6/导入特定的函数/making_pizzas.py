#可以导入模块中的特定函数：
#from module_name import function_name
#通过逗号分割函数名，可根据需要从模块中导入任意数量的函数:
#from module_name import function_0,function_1,function_3
from pizza import make_pizza
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')