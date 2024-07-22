import flet as ft
from time import sleep

def main(page: ft.Page):
    # lv = ft.ListView(expand=True, spacing=5, padding=0)
    # for i in range(1000):
    #     lv.controls.append(ft.Text(f"Line {i}"))
    def btn_clicked(e):
        lv.controls.append(ft.Text(f"Line"))
        page.update()
    page.padding = 0
    btn = ft.FilledButton(text='add', width=100, on_click=btn_clicked)
    lv = ft.ListView(expand=True, spacing=5, padding=0)
    page.add(btn, lv)

ft.app(target=main)
