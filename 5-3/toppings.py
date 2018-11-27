#测试多个条件
#如果顾客点了两种配料，就需要确保在其披萨中包含这些配料：
requested_toppings = ['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
    print("\nFinished making your pizza!")
