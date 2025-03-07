from home_page_add_new_song_elements import *
import flet as ft
import sqlite3
import shutil
import os
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
songs_mp3_data_folder_path = "C:/Users/User/PycharmProjects/pythonProject5/songs_mp3_data"
songs_img_data_folder_path = "C:/Users/User/PycharmProjects/pythonProject5/songs_img_data"

# Создание папок, если они не существуют
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


def add_new_song_to_data(e):
    global mp3_file_name, img_file_name, audio_length, selected_file_img, selected_file_mp3
    if img_file_name == None:
        print("BAD_img")
        return "add_song_snack_bar_open_no_mp3_data"
    elif mp3_file_name == None:
        print("BAD_mp3")
        return "add_song_snack_bar_open_no_img_data"

    path_to_img = f"{songs_img_data_folder_path}/{img_file_name}" if img_file_name else ""
    path_to_mp3 = f"{songs_mp3_data_folder_path}/{mp3_file_name}" if mp3_file_name else ""
    print(path_to_mp3,path_to_img)
    print(audio_length)

    if any(field.value == "" for field in [song_name_field, author_field, genre_field, album_field]):
        print("add_song_snack_bar_open_no_field_data")
        return "add_song_snack_bar_open_no_field_data"
    else:
        try:
            return 0
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
            cur.execute("INSERT INTO Songs_data (name, author, genre, album, mp3_file_long, path_to_mp3, path_to_img) VALUES(?,?,?,?,?,?,?,?)",
                        values)
            db.commit()

            return "open_song_snack_bar_new_song_added"
        except sqlite3.Error as e:
            return "add_song_snack_bar_open_already"
        finally:
            cur.close()
            db.close()


def update_songs_view():
    j = 1
    db = sqlite3.connect('User_songs_information.data')
    cur = db.cursor()
    cur.execute("SELECT * FROM Songs_data")
    songs = cur.fetchall()
    print(songs)

    for i in range(40):
        list_tile = ft.CupertinoListTile(
            additional_info=ft.Text("0"),
            leading=ft.Image(
                src="https://murkosha.ru/sites/default/files/styles/adaptive/public/news/2022/nikitis_i_sedrik.jpg?itok=KOsbDKW6",
                height=80, width=80, fit=ft.ImageFit.COVER, border_radius=15),
            leading_size=80,
            leading_to_title=18,
            title=ft.Text("0"),
            subtitle=ft.Text("0"),
            trailing=ft.Icon(name=ft.cupertino_icons.ALARM),
            on_click=click_on_cong,
            height=90,
        )
        all_songs_column.controls.append(list_tile)
        all_songs_column.controls.append(ft.Divider())
    for i in all_songs_column.controls:
        if isinstance(i, ft.CupertinoListTile):
            i.title = ft.Text(value=f"Anime{j}")
            j += 1
            print(i.title)

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


songs_home_column = ft.Column([], scroll=ft.ScrollMode.ALWAYS)
