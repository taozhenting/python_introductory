#专辑
def make_album(singer_name,album_name,song_number=''):
    albums = {
        'singer':singer_name,
        'album':album_name
    }
    if song_number:
        albums['song_number'] = song_number
    return albums
musician = make_album('taozhenting','xiaoyequ')
print(musician)
musician2 = make_album('weiyun','erge','10')
print(musician2)
musician3 = make_album('beiduofeng','dijiujiaoxiangqu','20')
print(musician3)