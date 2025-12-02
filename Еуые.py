import flet as ft
import flet_audio as fa


url = "C:/Users/User/PycharmProjects/MP3-player-on-Python-Flet/App_Data/Songs_Data/songs_mp3_data/BOOM - Evil (Official Video).mp3"


def main(page: ft.Page):
    def volume_down(_):
        audio1.volume -= 0.1
        audio1.update()

    def volume_up(_):
        audio1.volume += 0.1
        audio1.update()

    def balance_left(_):
        audio1.balance -= 0.1
        audio1.update()

    def balance_right(_):
        audio1.balance += 0.1
        audio1.update()

    def play(_):
        audio1.play()

    def pause(_):
        audio1.pause()

    def resume(_):
        audio1.resume()

    def release(_):
        audio1.release()

    def seek(_):
        print()

    def get_duration(_):
        print("Current duration:", audio1.get_duration())

    def get_position(_):
        print("Current position:", audio1.get_current_position())

    audio1 = fa.Audio(
        src=url,
        autoplay=False,
        volume=1,
        balance=0,
        on_loaded=lambda _: print("Loaded"),
        on_duration_changed=lambda e: print("Duration changed:", e),
        on_position_changed=lambda e: print("Position changed:", e),
        on_state_changed=lambda e: print("State changed:", e),
        on_seek_complete=lambda _: print("Seek complete"),
    )
    page.overlay.append(audio1)
    page.add(
        ft.ElevatedButton("Play", on_click=play),
        ft.ElevatedButton("Pause", on_click=pause),
        ft.ElevatedButton("Resume", on_click=resume),
        ft.ElevatedButton("Release", on_click=release),
        ft.ElevatedButton("Seek 3s", on_click=seek),
        ft.Row(
            [
                ft.ElevatedButton("Volume down", on_click=volume_down),
                ft.ElevatedButton("Volume up", on_click=volume_up),
            ]
        ),
        ft.Row(
            [
                ft.ElevatedButton("Balance left", on_click=balance_left),
                ft.ElevatedButton("Balance right", on_click=balance_right),
            ]
        ),
        ft.ElevatedButton("Get duration", on_click=get_duration),
        ft.ElevatedButton("Get current position", on_click=get_position),
    )


ft.app(main)