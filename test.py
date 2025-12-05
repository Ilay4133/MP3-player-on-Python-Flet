import flet as ft
import threading
import time


def main(page: ft.Page):
    page.title = "Song Slider"
    page.update()

    song_duration = 180  # длина песни в секундах
    current_time = 0  # текущее время
    is_running = True  # флаг работы "таймера"
    is_dragging = False  # флаг перетаскивания слайдера

    # ---- СЛАЙДЕР ----
    def slider_changed(e):
        nonlocal current_time, is_dragging
        if is_dragging:
            current_time = slider.value

    def slider_drag_start(e):
        nonlocal is_dragging
        is_dragging = True

    def slider_drag_end(e):
        nonlocal is_dragging
        is_dragging = False
        # Обновляем значение при отпускании слайдера
        current_time = slider.value
        page.update()

    slider = ft.Slider(
        min=0,
        max=song_duration,
        value=0,
        expand=True,
        on_change=slider_changed,
        on_change_start=slider_drag_start,
        on_change_end=slider_drag_end
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
            if is_running and not is_dragging:
                slider.value = current_time
                page.update()
                current_time += 0.01
            time.sleep(0.01)

    threading.Thread(target=update_slider, daemon=True).start()


ft.app(target=main)
