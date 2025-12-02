import flet as ft


song_name_field= ft.TextField(value="", label="Название",label_style=ft.TextStyle(color='#0ba6bf',size=22), width=500,border_color='#00718f',
                              cursor_color='#00718f',focused_border_color='#0ba6bf',border_radius=10,text_style=ft.TextStyle(color='#e8eee7',size=29),
                             border_width=2,selection_color='#81bece',cursor_width=4)
author_field = ft.TextField(value="", label="Артист",label_style=ft.TextStyle(color='#0ba6bf',size=22), width=500,border_color='#00718f',
                                   cursor_color='#00718f',focused_border_color='#0ba6bf',border_radius=10,text_style=ft.TextStyle(color='#e8eee7',size=29),
                             border_width=2,selection_color='#81bece',cursor_width=4)
genre_field = ft.TextField(value="", label="Жанр",label_style=ft.TextStyle(color='#0ba6bf',size=22), width=500,border_color='#00718f',
                                   cursor_color='#00718f',focused_border_color='#0ba6bf',border_radius=10,text_style=ft.TextStyle(color='#e8eee7',size=29),
                             border_width=2,selection_color='#81bece',cursor_width=4)
album_field=ft.TextField(value="", label="Альбом",label_style=ft.TextStyle(color='#0ba6bf',size=22), width=500,border_color='#00718f',
                        cursor_color='#00718f',focused_border_color='#0ba6bf',border_radius=10,text_style=ft.TextStyle(color='#e8eee7',size=29),
                             border_width=2,selection_color='#81bece',cursor_width=4)

all_songs_column=ft.Column(controls=[],scroll=ft.ScrollMode.ALWAYS,height=700)



