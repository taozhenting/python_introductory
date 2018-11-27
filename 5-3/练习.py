#判断外星人是否为绿色
alien_color = 'green'
if alien_color == 'green':
    print("玩家射杀外星人获得5个点")

alien_color = 'red'
if alien_color == 'green':
    print("玩家射杀外星人获得5个点")

#增加else
alien_color = 'green'
if alien_color == 'green':
    print("玩家射杀外星人获得5个点")
else:
    print("玩家获得10个点")

alien_color = 'red'
if alien_color == 'green':
    print("玩家射杀外星人获得5个点")
else:
    print("玩家获得10个点")

#增加elif
alien_color = 'green'
if alien_color == 'green':
    print("玩家获得5个点")
elif alien_color == "yellow":
    print("玩家获得10个点")
else:
    print("玩家获得15个点")

alien_color = 'yellow'
if alien_color == 'green':
    print("玩家获得5个点")
elif alien_color == "yellow":
    print("玩家获得10个点")
else:
    print("玩家获得15个点")

alien_color = 'red'
if alien_color == 'green':
    print("玩家获得5个点")
elif alien_color == "yellow":
    print("玩家获得10个点")
else:
    print("玩家获得15个点")

#根据age的值判断处于人生哪个阶段
age = 100
if age < 2:
    print("你是个婴儿")
elif age < 4:
    print("你正蹒跚学步")
elif age < 13:
    print("你是儿童")
elif age < 20:
    print("你是青少年")
elif age < 65:
    print("你是成年人")
else:
    print("你是老年人")

#检查水果
favorite_fruits = ['apple','orange','pear']
if 'apple' in favorite_fruits:
    print('You really like apple!')
if 'bananas' in favorite_fruits:
    print('You really like bananas!')
if 'orange' in favorite_fruits:
    print('You really like orange!')
if 'peach' in favorite_fruits:
    print('You really like peach!')
if 'pear' in favorite_fruits:
    print('You really like pear!')

