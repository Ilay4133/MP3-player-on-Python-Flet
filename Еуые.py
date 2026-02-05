import flet as ft
import flet_audio as fa


url = "C:/Users/Ilay_/PycharmProjects/MP3-player-on-Python-Flet/App_Data/Songs_Data/songs_mp3_data/Белый Фосфор『 ExTeam 』- Official Track ｜ Lyrics ｜ 2K.mp3"


def main(page: ft.Page):
    async def volume_down(_):
        audio1.volume -= 0.1
        audio1.update()

    async def volume_up(_):
        audio1.volume += 0.1
        audio1.update()

    async def balance_left(_):
        audio1.balance -= 0.1
        audio1.update()

    async def balance_right(_):
        audio1.balance += 0.1
        audio1.update()

    async def play(_):
        await audio1.play()

    async def pause(_):
        await audio1.pause()

    async def resume(_):
        await audio1.resume()

    async def release(_):
        await audio1.release()

    async def seek(_):
        print()

    async def get_duration(_):
        print("Current duration:", audio1.get_duration())

    async def get_position(_):
        print("Current position:", audio1.get_current_position())

    audio1 = fa.Audio(
        src=url,
        autoplay=False,
        volume=1,
        balance=0,
        on_loaded=lambda _: print("Loaded"),
        on_duration_change=lambda e: print("Duration changed:", e),
        on_position_change=lambda e: print("Position changed:", e),
        on_state_change=lambda e: print("State changed:", e),
        on_seek_complete=lambda _: print("Seek complete"),
    )

    page.add(
        ft.Button("Play", on_click=play),
        ft.Button("Pause", on_click=pause),
        ft.Button("Resume", on_click=resume),
        ft.Button("Release", on_click=release),
        ft.Button("Seek 3s", on_click=seek),
        ft.Row(
            [
                ft.Button("Volume down", on_click=volume_down),
                ft.Button("Volume up", on_click=volume_up),
            ]
        ),
        ft.Row(
            [
                ft.Button("Balance left", on_click=balance_left),
                ft.Button("Balance right", on_click=balance_right),
            ]
        ),
        ft.Button("Get duration", on_click=get_duration),
        ft.Button("Get current position", on_click=get_position),
    )


ft.app(main)