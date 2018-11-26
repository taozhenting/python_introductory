#切片，前三名队员
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
#索引1到4队员
print(players[1:4])
#从开头到4队员
print(players[:4])
#索引从2到最后队员
print(players[2:])
#最后三名队员
print(players[-3:])

#打印前三名队员
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

