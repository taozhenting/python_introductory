#嘉宾名单
names=['tom','alex','cherry']
#邀请嘉宾
print(names[0].title() + ' invites you to dinner.')
print(names[1].title() + ' invites you to dinner.')
print(names[2].title() + ' invites you to dinner.')
#tom无法赴约
print('\n' + names[0].title() + " can't keep the appointment.")

#删除tom
del names[0]
#修改成tao
names.insert(0,'tao')
#邀请嘉宾
print(names[0].title() + ' invites you to dinner.')
print(names[1].title() + ' invites you to dinner.')
print(names[2].title() + ' invites you to dinner.')

#发现更大的餐桌
print('\nCongratulations, I found a bigger table.')

#增加新嘉宾到开头
names.insert(0,'jones')
#增加新嘉宾到中间
names.insert(2,'sam')
#增加到新嘉宾到列尾
names.append('max')

#邀请嘉宾
print(names[0].title() + ' invites you to dinner.')
print(names[1].title() + ' invites you to dinner.')
print(names[2].title() + ' invites you to dinner.')
print(names[3].title() + ' invites you to dinner.')
print(names[4].title() + ' invites you to dinner.')
print(names[5].title() + ' invites you to dinner.')

#新购餐桌无法及时送达，因此只能邀请两位嘉宾
print('\nSorry, the new table is not served in time. Only two guests can be invited.')

#删除四位嘉宾，并告知无法邀请晚餐
lost_guest=names[-1]
names.remove(lost_guest)
print('Sorry, ' + lost_guest + ", I can't invite you to dinner.")

lost_guest=names[-1]
names.remove(lost_guest)
print('Sorry, ' + lost_guest + ", I can't invite you to dinner.")

lost_guest=names[-1]
names.remove(lost_guest)
print('Sorry, ' + lost_guest + ", I can't invite you to dinner.")

lost_guest=names[-1]
names.remove(lost_guest)
print('Sorry, ' + lost_guest + ", I can't invite you to dinner.")

#通知余下两位嘉宾可以参加晚餐
print('Congratulations, ' + names[0] + ', you can have dinner.')
print('Congratulations, ' + names[1] + ', you can have dinner.')

#删除两位嘉宾，让列表保持为空
names=[]
print('嘉宾列表是' + str(names))