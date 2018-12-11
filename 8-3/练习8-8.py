#专辑
def make_album(singer_name,album_name,song_number=''):
    albums = {
        'singer':singer_name,
        'album':album_name
    }
    if song_number:
        albums['song_number'] = song_number
    return albums

#编写while循环，让用户输入歌手，专辑，歌曲数
while True:
    print("\n(enter 'q' at any time to quit)")
    n_singer = input("请输入歌手姓名:")
    if n_singer == 'q':
        break
    n_album = input("请输入专辑名字:")
    if n_album == 'q':
        break
    n_song = input("请输入歌曲数:")
    if n_song == 'q':
        break
    musician = make_album(n_singer,n_album,n_song)
    print(musician)