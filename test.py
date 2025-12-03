import flet as ft
import threading
import time


def main(page: ft.Page):
    page.title = "Song Slider"
    page.update()

    song_duration = 180       # длина песни в секундах
    current_time = 0          # текущее время
    is_running = True         # флаг работы "таймера"

    # ---- СЛАЙДЕР ----
    slider = ft.Slider(
        min=0,
        max=song_duration,
        value=0,
        expand=True
    )

    # ---- КНОПКА СТОП/СТАРТ ----
    def toggle_run(e):
        nonlocal is_running
        is_running = not is_running
        btn.text = "Старт" if not is_running else "Пауза"
        page.update()

    btn = ft.ElevatedButton("Пауза", on_click=toggle_run)

    page.add(slider, btn)

    # ---- ПОТОК ОБНОВЛЕНИЯ ----
    def update_slider():
        nonlocal current_time

        while current_time <= song_duration:
            if is_running:
                slider.value = current_time
                page.update()
                current_time += 0.01

            time.sleep(0.01)

    threading.Thread(target=update_slider, daemon=True).start()


ft.app(target=main)
