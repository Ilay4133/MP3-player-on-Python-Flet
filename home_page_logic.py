from home_page_add_new_song_elements import *
import flet as ft
import sqlite3
import shutil
import os

sohgs_mp3_data_folder_path = "C:/Users/User/PycharmProjects/pythonProject5/songs_mp3_data"

sohgs_img_data_folder_path = "C:/Users/User/PycharmProjects/pythonProject5/songs_img_data"

if not os.path.exists(sohgs_mp3_data_folder_path):
    os.makedirs(sohgs_mp3_data_folder_path)

if not os.path.exists(sohgs_img_data_folder_path):
    os.makedirs(sohgs_img_data_folder_path)

db = sqlite3.connect('User_songs_information.data')
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Songs (
                name TEXT PRIMARY KEY,
                author TEXT,
                genre TEXT,
                album TEXT,
                path_to_mp3 TEXT,
                path_to_img TEXT)""")
cur.close()
db.close()

def add_new_song_to_data(e):

    path_to_mp3=""
    path_to_img = ""

    if any(field.value == "" for field in
           [song_name_field, author_field, genre_field, album_field]):
        return "add_song_snack_bar_open_no_data"
    else:
        try:
            db = sqlite3.connect('User_songs_information.data')
            cur = db.cursor()
            values = (
                str(song_name_field.value),
                str(author_field.value),
                str(genre_field.value),
                str(album_field.value),
                path_to_mp3,
                path_to_img
            )
            cur.execute("INSERT INTO Songs (name, author, genre, album, path_to_mp3, path_to_img) VALUES(?,?,?,?,?,?)",
                        values)
            db.commit()
            return "open_dialg"
        except sqlite3.Error as e:
            return "add_song_snack_bar_open_allready"
        finally:
            cur.close()
            db.close()




songs_home_column=ft.Column([],scroll=ft.ScrollMode.ALWAYS)
