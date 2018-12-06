#三个外星人存入列表并打印
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

#创建30个外星人
aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

#显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

#显示创建了多少个外星人
print("Total number of aliens:" + str(len(aliens)))

#修改前三个外星人，如果是绿色修改
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
#显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

#增加条件，将黄色外星人修改
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[:5]:
    print(alien)
print("...")

