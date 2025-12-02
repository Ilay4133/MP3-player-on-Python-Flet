import time
import sqlite3
import asyncio



def open_song_player(e):
    song_data_list=[]
    song_name=e.control.title.value
    db=sqlite3.connect('../../User_songs_information.data')
    cur = db.cursor()
    cur.execute("SELECT * FROM Songs_data")
    song_data=cur.fetchall()
    for i in song_data:
        if i[0]==song_name:
            for j in i:
                song_data_list.append(j)
    cur.close()
    db.close()
    print(song_data_list)
    return song_data_list
