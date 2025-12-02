import flet as ft

AUDIO_SRC = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
# или локальный файл: AUDIO_SRC = "path/to/file.mp3"

def main(page: ft.Page):
    page.title = "Audio toggle (play/pause) example"

    # Audio — не визуальный контрол, поэтому добавляем в overlay
    audio = ft.Audio(src=AUDIO_SRC)
    page.overlay.append(audio)

    # Кнопка — будет менять иконку в зависимости от состояния
    play_pause_btn = ft.IconButton(
        icon=ft.Icons.PLAY_ARROW,
        tooltip="Play / Pause",
    )

    # Обработчик клика — запускает play() или pause() в зависимости от иконки.
    # Можно также использовать внутренний флаг, но иконка сама хранит видимую логику.
    async def on_toggle(e):
        # если кнопка показывает PLAY — запускаем воспроизведение
        if play_pause_btn.icon == ft.Icons.PLAY_ARROW:
            await audio.play()   # play(position=0) — можно передать позицию
        else:
            await audio.pause()

    play_pause_btn.on_click = on_toggle

    # Обработчик события изменения состояния плеера:
    # ставим иконку Pause когда играет, Play в остальных состояниях.
    def on_state_change(ev: ft.AudioStateChangeEvent):
        # ev.state — это значение из ft.AudioState (PLAYING, PAUSED, STOPPED, ...)
        if ev.state == ft.AudioState.PLAYING:
            play_pause_btn.icon = ft.Icons.PAUSE
        else:
            play_pause_btn.icon = ft.Icons.PLAY_ARROW
        play_pause_btn.update()

    audio.on_state_change = on_state_change

    # Небольшой интерфейс: кнопка и подпись
    page.add(
        ft.Column(
            [
                ft.Row([play_pause_btn, ft.Text("Нажмите, чтобы воспроизвести / поставить на паузу")]),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
