#创建字典
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

#增加字典的键和值
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#创建空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#修改字典中的值
alien_0 = {'color':'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

#给外星人添加速度
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position:" + str(alien_0['x_position']))
#判断速度，写入不同的x坐标
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position:" + str(alien_0['x_position']))
#如外星人速度改成fast,放到代码上面重新执行
alien_0['speed'] = 'fast'

#删除字典键值
alien_0 = {'color':'green','point':5}
print(alien_0)
del alien_0['point']
print(alien_0)

