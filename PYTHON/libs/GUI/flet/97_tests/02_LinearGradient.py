import flet as ft

def main(page: ft.Page) -> None:

    c = ft.Container(
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[ft.colors.BLUE, ft.colors.GREEN, ft.colors.YELLOW],
            stops=[0.0, 0.7, 1.0]
    
        ),
        width=150,
        height=150,
        border_radius=5,
    )

    page.add(c)

ft.app(main)
