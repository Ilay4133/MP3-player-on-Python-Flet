from registration_and_login import *
from registration_and_login_elements import *
from home_page_logic import *
from home_page_add_new_song_elements import *
import flet as ft



def main(page: ft.Page):

    page.title = "Регистрация"
    page.bgcolor='#0b012e'
    page.theme_mode=ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Центрирование по вертикали
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Центрирование по горизонтали
    page.pading=ft.padding.all(100)
    page.update()

    def snack_bar_open():
        snack_bar = ft.SnackBar(ft.Text(value="Вы не заполнили все поля", color='#e8eee7'), bgcolor='#0c3348')
        page.add(snack_bar)
        page.open(snack_bar)
        page.update()

    def snack_bar_open_whod():
        snack_bar = ft.SnackBar(ft.Text(value="Нет такого пользователя", color='#e8eee7'), bgcolor='#0c3348')
        page.add(snack_bar)
        page.open(snack_bar)
        page.update()

    def snack_bar_open_reg():
        snack_bar = ft.SnackBar(ft.Text(value="Такой пользователь уже есть (SQLite database Error)", color='#e8eee7'), bgcolor='#0c3348')
        page.add(snack_bar)
        page.open(snack_bar)
        page.update()



    class Open_reg():
        def open_user_panel(e):
            print("User panel")

        def open_admin_panel(e):
            print("Admin panel")

        def open_reg_window(e):
            reg_column.visible = True
            go_to_reg.visible = False
            go_to_vhod.visible = False
            back_start_but.visible = True
            vhod_in_text.visible = False
            page.update()

        def open_vhod_window(e):
            Close_reg.close_reg_window(1)
            vhod_column.visible = True
            go_to_reg.visible = False
            go_to_vhod.visible = False
            back_start_but.visible = True
            vhod_in_text.visible = False
            page.update()

        def open_vhod_window_lambda(e):
            global new_user_enter
            new_user_enter = 1
            Open_reg.open_vhod_window(1)
            close = lambda: page.close(dlg_reg)
            close()
            page.update()

    class Open_home():
        def open_add_new_song_wind(e):
            page.open(add_new_song_dlg)
            page.update()
        def open_select_songs_wind(e):
            pass
        def open_sort_songs_wind(e):
            pass
        def open_search_song_wind(e):
            pass
        def open_edit_design_wind(e):
            pass

    class Close_reg():
        def close_all(e):
            go_to_reg.visible = False
            vhod_in_text.visible = False
            go_to_vhod.visible = False
            back_start_but.visible = False

        def close_dlg(e):
            close = lambda: page.close(dlg_reg)
            close()

        def close_reg_window(e):
            name_field_reg.value = None
            last_name_field_reg.value = None
            otchestvo_field_reg.value = None
            pas_field_reg.value = None
            mail_field.value = None
            age_field_reg.value = None
            city_field_reg.value = None
            pol_vebor.value = None
            reg_column.visible = False
            page.update()

        def close_vhod_wind(self):
            name_field_login.value = None
            pas_field_login.value = None
            vhod_column.visible = False
            page.update()

        def back_start(self):
            Close_reg.close_reg_window(1)
            Close_reg.close_vhod_wind(1)
            go_to_reg.visible = True
            vhod_in_text.visible = True
            go_to_vhod.visible = True
            back_start_but.visible = False
            page.update()

    def select_but_chage(e):
        if int(e.data)==0:
            page_selecter_but.controls[5].color = '#688fa4';page_selecter_but.controls[1].color = '#688fa4';page_selecter_but.controls[2].color = '#688fa4'
            page_selecter_but.controls[3].color = '#688fa4';page_selecter_but.controls[4].color = '#688fa4';page_selecter_but.controls[0].color = '#e8eee7'
            page.update()

        elif int(e.data)==1:
            page_selecter_but.controls[0].color = '#688fa4';page_selecter_but.controls[5].color = '#688fa4';page_selecter_but.controls[2].color = '#688fa4'
            page_selecter_but.controls[3].color = '#688fa4';page_selecter_but.controls[4].color = '#688fa4';page_selecter_but.controls[1].color = '#e8eee7'
            page.update()

        elif int(e.data)==2:
            page_selecter_but.controls[0].color = '#688fa4';page_selecter_but.controls[1].color = '#688fa4';page_selecter_but.controls[5].color = '#688fa4'
            page_selecter_but.controls[3].color = '#688fa4';page_selecter_but.controls[4].color = '#688fa4';page_selecter_but.controls[2].color = '#e8eee7'
            page.update()

        elif int(e.data)==3:
            page_selecter_but.controls[0].color = '#688fa4';page_selecter_but.controls[1].color = '#688fa4';page_selecter_but.controls[2].color = '#688fa4'
            page_selecter_but.controls[5].color = '#688fa4';page_selecter_but.controls[4].color = '#688fa4';page_selecter_but.controls[3].color = '#e8eee7'
            page.update()

        elif int(e.data)==4:
            page_selecter_but.controls[0].color = '#688fa4';page_selecter_but.controls[1].color = '#688fa4';page_selecter_but.controls[2].color = '#688fa4'
            page_selecter_but.controls[3].color = '#688fa4';page_selecter_but.controls[5].color = '#688fa4';page_selecter_but.controls[4].color = '#e8eee7'
            page.update()

        elif int(e.data)==5:
            page_selecter_but.controls[0].color = '#688fa4';page_selecter_but.controls[1].color = '#688fa4';page_selecter_but.controls[2].color = '#688fa4'
            page_selecter_but.controls[3].color = '#688fa4';page_selecter_but.controls[4].color = '#688fa4';page_selecter_but.controls[5].color = '#e8eee7'
            page.update()

    def view_login(e):
        login_stat = login(1, name_field_login, pas_field_login)
        if login_stat == "snack_bar_open_whod":
            snack_bar_open_whod()
        elif login_stat == "open_admin_panel":
            Open_reg.open_admin_panel(1)
        elif login_stat == "open_user_panel":
            Open_reg.open_user_panel(1)

    def view_registration(e):
        registration_stat = registration(1, name_field_reg, last_name_field_reg, otchestvo_field_reg, pas_field_reg,
                                        age_field_reg, mail_field, pol_vebor, city_field_reg)
        if registration_stat == "snack_bar_open":
            snack_bar_open()
        elif registration_stat == "open_dialg":
            open_dlg = lambda: page.open(dlg_reg)
            open_dlg()
        elif registration_stat == "snack_bar_open_reg":
            snack_bar_open_reg()


    def add_song_snack_bar_open_no_mp3_data(page):
        snack_bar = ft.SnackBar(ft.Text(value="Не выбран mp3 файл", color='#e8eee7'), bgcolor='#0c3348')
        page.add(snack_bar)
        page.open(snack_bar)
        page.update()

    def add_song_snack_bar_open_no_img_data(page):
        snack_bar=ft.SnackBar(ft.Text("Не выбран .png / .jpg файл", color='#e8eee7'), bgcolor='#0c3348')
        page.add(snack_bar)
        page.open(snack_bar)
        page.update()


    def add_song_snack_bar_open_no_field_data(page):
        snack_bar = ft.SnackBar(ft.Text(value="Не заполнены все поля", color='#e8eee7'), bgcolor='#0c3348')
        page.add(snack_bar)
        page.open(snack_bar)
        page.update()

    def add_song_snack_bar_open_already(page):
        snack_bar = ft.SnackBar(ft.Text(value="Такая песня уже есть (SQLite database Error)", color='#e8eee7'),
                                     bgcolor='#0c3348')
        page.add(snack_bar)
        page.open(snack_bar)
        page.update()
    def open_song_snack_bar_new_song_added(page):
        snack_bar = ft.SnackBar(ft.Text(value="Песня добавлена", color='#e8eee7'), bgcolor='#0c3348')
        page.add(snack_bar)
        page.open(snack_bar)
        page.update()



    def view_add_new_song_to_data(e):
        add_new_song_return = add_new_song_to_data()
        if add_new_song_return=="add_song_snack_bar_open_no_mp3_data":
            page.close(add_new_song_dlg)
            add_song_snack_bar_open_no_mp3_data(page)

        elif add_new_song_return == "add_song_snack_bar_open_no_img_data":
            page.close(add_new_song_dlg)
            add_song_snack_bar_open_no_img_data(page)

        elif add_new_song_return == "add_song_snack_bar_open_no_field_data":
            page.close(add_new_song_dlg)
            add_song_snack_bar_open_no_field_data(page)

        elif add_new_song_return == "add_song_snack_bar_open_already":
            page.close(add_new_song_dlg)
            add_song_snack_bar_open_already(page)

        elif add_new_song_return == "open_song_snack_bar_new_song_added":
            page.close(add_new_song_dlg)
            open_song_snack_bar_new_song_added(page)

        page.update()


    # Элементы страницы регистрации
    reg_but = ft.ElevatedButton(content=ft.Text(value="Зарегистрироваться", color='#e8eee7',style=ft.TextStyle(size=17)),
                                on_click=view_registration,
                                bgcolor='#036380', style=ft.ButtonStyle(overlay_color='#0ba6bf'),width=200,height=35)
    dlg_reg = ft.AlertDialog(
        modal=True,
        title=ft.Text("Подтвердите пожалуйста",color='#e8eee7'),
        content=ft.Text("Хотите перейти ко входу?",color='#e8eee7'),
        actions=[
            ft.TextButton(text="Да", on_click=Open_reg.open_vhod_window_lambda,
                          style=ft.ButtonStyle(color='#e8eee7', bgcolor='#036380', overlay_color='#0ba6bf')),
            ft.TextButton(text="Нет", on_click=Close_reg.close_dlg,
                          style=ft.ButtonStyle(color='#e8eee7', bgcolor='#036380', overlay_color='#0ba6bf'))],
        actions_alignment=ft.MainAxisAlignment.END, bgcolor='#012f4a')

    reg = ft.Column([reg_text, name_field_reg, last_name_field_reg, otchestvo_field_reg, pas_field_reg, mail_field,
                     age_field_reg, pol_vebor, city_field_reg,
                     reg_but], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    reg_column = ft.Container(content=reg, alignment=ft.alignment.center, expand=True)

    # Элементы страницы входа
    vhod_but = ft.ElevatedButton(content=ft.Text(value="Вход", color='#e8eee7',style=ft.TextStyle(size=17)),
                                 on_click=view_login, bgcolor='#036380',
                                 style=ft.ButtonStyle(overlay_color='#0ba6bf'),width=200,height=35)
    vhod = ft.Column([vhod_text, name_field_login, pas_field_login, vhod_but], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    vhod_column = ft.Container(content=vhod, alignment=ft.alignment.center, expand=True)

    # Элементы начальной страницы
    vhod_in_text = ft.Text(value="Уже есть аккаунт?",style=ft.TextStyle(size=18,weight=ft.FontWeight.BOLD),color='#0ba6bf')
    go_to_reg = ft.ElevatedButton(content=ft.Text(value="Регистрация", color='#e8eee7',style=ft.TextStyle(size=17)), on_click=Open_reg.open_reg_window,
                                  bgcolor='#036380', style=ft.ButtonStyle(elevation=None, overlay_color='#0ba6bf'),width=155)
    go_to_vhod = ft.ElevatedButton(content=ft.Text(value="Войти ", color='#e8eee7',style=ft.TextStyle(size=17)), on_click=Open_reg.open_vhod_window,
                                   style=ft.ButtonStyle(elevation=None, overlay_color='#0ba6bf'),width=135,bgcolor='#231c3b')
    back_start_but = ft.ElevatedButton(content=ft.Text(value="Назад", color='#e8eee7',style=ft.TextStyle(size=17)), on_click=Close_reg.back_start,
                                       bgcolor='#036380', style=ft.ButtonStyle(elevation=None, overlay_color='#0ba6bf'),width=200,height=35)

    start = ft.Column([go_to_reg, vhod_in_text, go_to_vhod, back_start_but], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    start_column = ft.Container(content=start, alignment=ft.alignment.center, expand=True)

    page.add(ft.Column([vhod_column, reg_column, start_column], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True))
    Close_reg.back_start(1)
    page.update()
    # Элементы окна добавления новой песни
    mp3_file_picker = ft.FilePicker(on_result=pick_files_result_mp3)
    img_file_picker = ft.FilePicker(on_result=pick_files_result_img)

    add_path_to_mp3_but = ft.IconButton(icon=ft.Icons.AUDIO_FILE_ROUNDED,icon_size=70,tooltip="Добавить mp3 файл",
                                        icon_color = '#0ba6bf', hover_color = '#00457d',on_click=lambda _: mp3_file_picker.pick_files(
            allow_multiple=False,allowed_extensions=["mp3"]))

    add_path_to_img_but = ft.IconButton(icon=ft.Icons.ADD_PHOTO_ALTERNATE_ROUNDED,icon_size=70,tooltip="Добавить иконку",
                                        icon_color = '#0ba6bf', hover_color = '#00457d',on_click=lambda _: img_file_picker.pick_files(
            allow_multiple=False,allowed_extensions=["png","jpg"]))

    add_new_song_but = ft.ElevatedButton(content=ft.Row([ft.Icon(name=ft.Icons.ADD_ROUNDED,color='#e8eee7',size=40),
                                                         ft.Text("Добавить песню",size=26, color='#e8eee7')], alignment=ft.MainAxisAlignment.CENTER),
                                         bgcolor='#01315c',width=350,height=60,style=ft.ButtonStyle(overlay_color='#036380',elevation=15,shadow_color='#0ba6bf'),
                                         tooltip="Добавить песню в библиотеку",on_click=view_add_new_song_to_data)



    add_paths_row = ft.Row(controls=[add_path_to_mp3_but, add_path_to_img_but], alignment=ft.MainAxisAlignment.CENTER)

    add_new_song_dlg = ft.AlertDialog(
        modal=False,
        title=ft.Text("Добавление новой песни", color='#e8eee7',size=32),
        bgcolor='#14044d',
        shadow_color='#0ba6bf',
        elevation=100,
        shape=ft.ContinuousRectangleBorder(radius=60),
        actions=[
            ft.Column(
                [
                    song_name_field,
                    author_field,
                    genre_field,
                    album_field,
                    add_paths_row,
                    add_new_song_but
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            )
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )


    # Элементы домашней страницы (страницы с песнями)________________________
    drawer = ft.NavigationDrawer(
        on_dismiss=lambda e: print("close"),
        on_change=lambda e:print(e),
        indicator_color='#0ba6bf',
        bgcolor='#14044d',
        shadow_color='#0ba6bf',
        elevation=100,
        tile_padding=0,
        indicator_shape=ft.ContinuousRectangleBorder(radius=20),
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Библиотека",
                icon=ft.Icons.MY_LIBRARY_MUSIC_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.MY_LIBRARY_MUSIC_ROUNDED),
            ),
            ft.Divider(thickness=1,color='#0ba6bf'),
            ft.NavigationDrawerDestination(
                label="Эквалайзер",
                icon=ft.Icon(ft.Icons.TUNE_SHARP),
                selected_icon=ft.Icons.TUNE_OUTLINED,
            ),
            ft.NavigationDrawerDestination(
                label="Таймер сна",
                icon=ft.Icon(ft.Icons.ACCESS_TIME_ROUNDED),
                selected_icon=ft.Icons.ACCESS_TIME_FILLED_ROUNDED,
            ),
            ft.NavigationDrawerDestination(
                label="Настройки",
                icon=ft.Icon(ft.Icons.BRIGHTNESS_7_OUTLINED),
                selected_icon=ft.Icons.BRIGHTNESS_7_ROUNDED,
            ),
        ],
    )

    page_selecter_but=ft.CupertinoSlidingSegmentedButton(
        width=1600,height=50,bgcolor='#0b012e',thumb_color='#160454',on_change=select_but_chage,
        controls=[
        ft.Text(value="Песни",size=40,color='#688fa4'),
        ft.Text(value="Плейлисты",size=40,color='#688fa4'),
        ft.Text(value="Папки",size=40,color='#688fa4'),
        ft.Text(value="Альбомы",size=40,color='#688fa4'),
        ft.Text(value="Артисты",size=40,color='#688fa4'),
        ft.Text(value="Жанры",size=40,color='#688fa4')])

    vert_divider_home_menu=ft.VerticalDivider(width=20)
    vert_divider_songs_menu = ft.VerticalDivider(width=885)
    divider_home_page=ft.Divider(height=20,thickness=1,color='#0ba6bf')
    divider_home_songs_page = ft.Divider(height=10, thickness=0 ,color='#0b012e')

    search_icon_but=ft.IconButton(icon=ft.Icons.SEARCH_SHARP,icon_size=50,icon_color='#0ba6bf',
                                  tooltip="Поиск в библиотеке",hover_color='#00457d',on_click=Open_home.open_search_song_wind)
    design_icon_but=ft.IconButton(icon=ft.Icons.COLOR_LENS_ROUNDED,icon_size=50,icon_color='#0ba6bf',
                                  tooltip="Изменить тему",hover_color='#00457d',on_click=Open_home.open_edit_design_wind)
    menu_icon_but=ft.IconButton(icon=ft.Icons.MENU_OPEN_SHARP,icon_size=50,icon_color='#0ba6bf',
                                  tooltip="Меню",hover_color='#00457d',on_click=lambda e: page.open(drawer))
    songs_list_icon_but=ft.IconButton(icon=ft.Icons.FORMAT_LIST_NUMBERED,icon_size=50,icon_color='#0ba6bf',
                                  tooltip="Выбрать песни",hover_color='#00457d',on_click=Open_home.open_select_songs_wind)
    sorting_icon_but=ft.IconButton(icon=ft.Icons.ALT_ROUTE_SHARP,icon_size=50,icon_color='#0ba6bf',
                                  tooltip="Сортировать",hover_color='#00457d',on_click=Open_home.open_sort_songs_wind)
    add_new_song_icon_but=ft.IconButton(icon=ft.Icons.ADD_CIRCLE_OUTLINE_ROUNDED,icon_size=50,icon_color='#0ba6bf',
                                  tooltip="Добавить песню",hover_color='#00457d',on_click=Open_home.open_add_new_song_wind)

    reproduce_icon=ft.Icon(name=ft.Icons.PLAY_ARROW_ROUNDED,color='#e3a112',size=45)
    reproduce_text=ft.Text(value="Воспроизвести",size=32,color='#e8eee7')
    reproduce_but=ft.ElevatedButton(content=ft.Row([reproduce_icon,reproduce_text]),bgcolor='#01315c',
                                      height=55,width=310,style=ft.ButtonStyle(overlay_color='#036380'))

    random_sort_icon = ft.Icon(name=ft.Icons.SHUFFLE_SHARP, color='#e3a112', size=45)
    random_sort_text = ft.Text(value="Перемешать", size=32, color='#e8eee7')
    random_sort_but = ft.ElevatedButton(content=ft.Row([random_sort_icon, random_sort_text]), bgcolor='#01315c',
                                        height=55, width=270,style=ft.ButtonStyle(overlay_color='#036380'))

    songs_count_text=ft.Text(value="X Песен",size=31,color='#e8eee7')

    songs_count_text_cont=ft.Container(content=songs_count_text,padding=ft.Padding(top=0,left=15,right=0,bottom=0))


    home_menus_buttons=ft.Row([menu_icon_but,design_icon_but,search_icon_but,vert_divider_home_menu,page_selecter_but])
    songs_menus_elements=ft.Row([songs_count_text_cont,vert_divider_songs_menu,add_new_song_icon_but,random_sort_but,reproduce_but,sorting_icon_but,songs_list_icon_but])

    home_page_column=ft.Column([home_menus_buttons,divider_home_page,songs_menus_elements,divider_home_songs_page])
    page.add(home_page_column,all_songs_column)
    page.add(add_new_song_dlg)
    page.update()
    page.padding=ft.Padding(top=20,left=30,right=30,bottom=80)
    start_column.visible=False
    page.close(add_new_song_dlg)
    page.add(mp3_file_picker,img_file_picker)
    update_songs_view()

    page.update()


ft.app(target=main)
# flet run view.py --web
