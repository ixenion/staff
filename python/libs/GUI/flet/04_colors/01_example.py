import flet as ft

def main(page: ft.Page) -> None:
    page.title = "Change container bgcolor property"            

    def change_bgcolor(e):
        container.bgcolor = new_color.value
        new_color.value = ""

        container.update()
        new_color.update()

    container = ft.Container(
        width=200, height=200, bgcolor=ft.colors.CYAN, border=ft.border.all(1, ft.colors.BLACK)
    )
    new_color = ft.TextField(
        label="Hex value in format #AARRGGBB or #RRGGBB", width=500
    )

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # page.horizontal_alignment = "center"
    page.add(ft.Column(
        controls=[
            container,
            ft.Row(
                controls=[
                    new_color,
                    ft.FilledButton(
                        text="Change container bgcolor", on_click=change_bgcolor
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    )
ft.app(target=main) 
