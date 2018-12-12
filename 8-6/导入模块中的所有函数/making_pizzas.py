#使用星号可让python导入模块所有函数
from pizza import *
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
#在导入并非自己写的大型模块时，最好不要采用这种导入方法。如果模块中函数和你项目中名称相同
#会有意想不到结果，如果要导入所有函数，尽量使用：
#import pizza
#pizza.make_pizza
#导入整个模块，并使用句点表示法。