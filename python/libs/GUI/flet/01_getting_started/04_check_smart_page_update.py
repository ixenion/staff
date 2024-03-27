import flet as ft
from time import sleep

def main(page: ft.Page):
    
    for i in range(10):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            page.controls.pop(0)
        # sleep(0.3)
    page.update()
    pass

# run as desctop
ft.app(target=main)
