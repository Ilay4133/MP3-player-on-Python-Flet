from home_page_add_new_song_elements import *
import flet as ft
import sqlite3
import shutil
import os
import random
from mutagen.mp3 import MP3

# Инициализация глобальных переменных
global mp3_file_name
global img_file_name
global audio_length
global selected_file_img
global selected_file_mp3

mp3_file_name = None
img_file_name = None
audio_length = None
selected_file_img = None
selected_file_mp3 = None


# Пути к папкам
songs_mp3_data_folder_path = "C:/Users/User/PycharmProjects/pythonProject3/songs_mp3_data"
songs_img_data_folder_path = "C:/Users/User/PycharmProjects/pythonProject/songs_img_data"

Создание папок, если они не существуют
if not os.path.exists(songs_mp3_data_folder_path):
    os.makedirs(songs_mp3_data_folder_path)

if not os.path.exists(songs_img_data_folder_path):
    os.makedirs(songs_img_data_folder_path)

# Подключение к базе данных
db = sqlite3.connect('User_songs_information.data')
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Songs_data (
                name TEXT PRIMARY KEY,
                author TEXT,
                genre TEXT,
                album TEXT,
                mp3_file_long TEXT,
                path_to_mp3 TEXT,
                path_to_img TEXT)""")
cur.close()
db.close()


def add_new_song_to_data():
    global mp3_file_name, img_file_name, audio_length, selected_file_img, selected_file_mp3
    if img_file_name == None:
        print("BAD_img")
        return "add_song_snack_bar_open_no_img_data"
    elif mp3_file_name == None:
        print("BAD_mp3")
        return "add_song_snack_bar_open_no_mp3_data"

    path_to_img = f"{songs_img_data_folder_path}/{img_file_name}" if img_file_name else ""
    path_to_mp3 = f"{songs_mp3_data_folder_path}/{mp3_file_name}" if mp3_file_name else ""

    if any(field.value == "" for field in [song_name_field, author_field, genre_field, album_field]):
        print("add_song_snack_bar_open_no_field_data")
        return "add_song_snack_bar_open_no_field_data"
    else:
        try:
            db = sqlite3.connect('User_songs_information.data')
            cur = db.cursor()
            values = (
                str(song_name_field.value),
                str(author_field.value),
                str(genre_field.value),
                str(album_field.value),
                audio_length,
                path_to_mp3,
                path_to_img
            )
            cur.execute("INSERT INTO Songs_data (name, author, genre, album, mp3_file_long, path_to_mp3, path_to_img) VALUES(?,?,?,?,?,?,?)",
                        values)
            db.commit()
        except sqlite3.Error as e:
            return "add_song_snack_bar_open_already"
        finally:
            cur.close()
            db.close()
            update_songs_view()
            return "open_song_snack_bar_new_song_added"


def update_songs_view(songs_count_text):
    all_songs_column.controls.clear()
    db = sqlite3.connect('User_songs_information.data')
    cur = db.cursor()
    cur.execute("SELECT * FROM Songs_data")
    songs = cur.fetchall()



    for i in songs:
        list_tile = ft.CupertinoListTile(
            additional_info=ft.Text(value=f"no data",color='#e8eee7',size=22),
            leading=ft.Image(
                src="https://murkosha.ru/sites/default/files/styles/adaptive/public/news/2022/nikitis_i_sedrik.jpg?itok=KOsbDKW6",
                height=80, width=80, fit=ft.ImageFit.COVER, border_radius=15),
            leading_size=80,
            leading_to_title=18,
            title=ft.Text(value=f"no data",color='#e8eee7',size=35),
            subtitle=ft.Text(value=f"no data",color='#a1a6a1',size=19),
            on_click=click_on_cong,
            height=90,
        )
        all_songs_column.controls.append(list_tile)
        all_songs_column.controls.append(ft.Divider())
    songs_count_text.value=f"{len(songs)} Песен"



    for i in all_songs_column.controls[::2]:
        element_index = all_songs_column.controls.index(i)
        i.additional_info.value=f"{songs[element_index//2][4]}          "
        i.leading.src=f"{songs[element_index//2][6]}"
        i.title.value=f"{songs[element_index//2][0]}"
        i.subtitle.value=f"{songs[element_index//2][1]} - {songs[element_index//2][3]}"
    all_songs_column.update()
    cur.close()
    db.close()


def pick_files_result_mp3(e: ft.FilePickerResultEvent):
    global mp3_file_name, selected_file_mp3, audio_length

    if e.files:
        mp3_file_name = e.files[0].name
        selected_file_mp3 = e.files[0].path
        try:
            shutil.copy(selected_file_mp3, songs_mp3_data_folder_path)
            audio = MP3(f"{songs_mp3_data_folder_path}/{mp3_file_name}")
            length_in_seconds = audio.info.length
            minutes = int(length_in_seconds // 60)
            if int(length_in_seconds % 60)>10:
                seconds = f"0{int(length_in_seconds % 60)}"
            else:
                seconds = int(length_in_seconds % 60)
            audio_length = f"{minutes}:{seconds}"
        except Exception as ex:
            return ex
    else:
        return "snack_bar_file_not_caught"


def pick_files_result_img(e: ft.FilePickerResultEvent):
    global img_file_name, selected_file_img

    if e.files:
        img_file_name = e.files[0].name
        selected_file_img = e.files[0].path
        try:
            shutil.copy(selected_file_img, songs_img_data_folder_path)
        except Exception as ex:
            return ex
    else:
        return "snack_bar_file_not_caught"

def random_sort_all_songs_column():
    songs = [item for item in all_songs_column.controls if isinstance(item, ft.CupertinoListTile)]
    dividers = [item for item in all_songs_column.controls if isinstance(item, ft.Divider)]
    random.shuffle(songs)
    random_song_column = []
    song_index = 0
    for item in all_songs_column.controls:
        if isinstance(item, ft.Divider):
            random_song_column.append(item)
        else:
            random_song_column.append(songs[song_index])
            song_index += 1

    return random_song_column

songs_home_column = ft.Column([], scroll=ft.ScrollMode.ALWAYS)
