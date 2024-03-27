import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    # page content alligment
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

# run as desctop
ft.app(target=main)
# run as web
# ft.app(target=main, view=ft.WEB_BROWSER)
