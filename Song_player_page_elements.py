import flet as ft


song_player_img = ft.Image(src="https://cdn-images.dzcdn.net/images/cover/1cd5e403161bfc42357d759b06e63f0e/0x1900-000000-80-0-0.jpg",
                               height=600, width=600, fit=ft.ImageFit.COVER)

song_player_name_text = ft.Text(value="НАЗВАНИЕ",selectable=True,size=50, color='#e8eee7')
song_player_author_genre_text = ft.Text(value="АВТОР - ЖАНР",selectable=True,size=50, color='#e8eee7')
song_player_song_text = ft.Text(value="ТЕКСТ ПЕСНИ",selectable=True, color='#e8eee7')

song_like_icon_but = ft.IconButton(icon=ft.Icons.FAVORITE_BORDER_ROUNDED, icon_size=60,tooltip="Добавить в избранное"
                                    ,icon_color='#0ba6bf',hover_color='#00457d') #Icons.FAVORITE_ROUNDED
song_add_to_playlist_icon_but = ft.IconButton(icon=ft.Icons.LIBRARY_ADD_ROUNDED, icon_size=60, tooltip="Добавить в плейлист"
                                    ,icon_color='#0ba6bf',hover_color='#00457d')
song_ecvalizer_icon_but = ft.IconButton(icon=ft.Icons.TUNE_ROUNDED, icon_size=60, tooltip="Эквалайзер"
                                    ,icon_color='#0ba6bf',hover_color='#00457d')
song_timer_icon_but = ft.IconButton(icon=ft.Icons.ACCESS_TIME_ROUNDED, icon_size=60, tooltip="Остановить музыку через ..."
                                    ,icon_color='#0ba6bf',hover_color='#00457d')
songs_queue_icon_but = ft.IconButton(icon=ft.Icons.FORMAT_INDENT_INCREASE_ROUNDED, icon_size=60, tooltip="Очередь"
                                    ,icon_color='#0ba6bf',hover_color='#00457d')
back_song_time_icon_but = ft.IconButton(icon=ft.Icons.REPLAY_10_ROUNDED, icon_size=60, tooltip="-10 сек."
                                    ,icon_color='#0ba6bf',hover_color='#00457d')
forward_song_time_icon_but = ft.IconButton(icon=ft.Icons.FORWARD_10_ROUNDED, icon_size=60, tooltip="+10 сек."
                                    ,icon_color='#0ba6bf',hover_color='#00457d')
song_player_design_icon_but = ft.IconButton(icon=ft.Icons.COLOR_LENS_ROUNDED, icon_size=60, tooltip="Изменить тему"
                                    ,icon_color='#0ba6bf',hover_color='#00457d')
song_player_additinol_icon_but = ft.IconButton(icon=ft.Icons.MORE_VERT_ROUNDED, icon_size=60, tooltip="Дополнительно"
                                    ,icon_color='#0ba6bf',hover_color='#00457d')

song_play_slider = ft.Slider(width=950, max=100, min=0, secondary_active_color='#0ba6bf', overlay_color='#41a9ba',
                             active_color='#0ba6bf', inactive_color='#1a0257', thumb_color='#e3a112')

song_player_random_sort_icon_but = ft.IconButton(icon=ft.Icons.SHUFFLE_SHARP, icon_size=60, tooltip="Перемешать"
                                    ,icon_color='#0ba6bf',hover_color='#00457d')
song_player_previous_song_icon_but = ft.IconButton(icon=ft.Icons.SKIP_PREVIOUS_ROUNDED, icon_size=60, tooltip="Предыдущая "
                                    ,icon_color='#0ba6bf',hover_color='#00457d')
song_player_play_song_icon_but = ft.IconButton(icon=ft.Icons.PLAY_CIRCLE_FILLED_ROUNDED, icon_size=60, tooltip="Запустить"
                                    ,icon_color='#0ba6bf',hover_color='#00457d') #Icons.PAUSE_CIRCLE_ROUNDED
song_player_next_song_icon_but = ft.IconButton(icon=ft.Icons.SKIP_NEXT_ROUNDED, icon_size=60, tooltip="Следующая"
                                    ,icon_color='#0ba6bf',hover_color='#00457d')
song_player_repeat_songs = ft.IconButton(icon=ft.Icons.REPEAT_ROUNDED, icon_size=60, tooltip="Повторять"
                                    ,icon_color='#0ba6bf',hover_color='#00457d') #Icons.REPEAT_ONE_ROUNDED