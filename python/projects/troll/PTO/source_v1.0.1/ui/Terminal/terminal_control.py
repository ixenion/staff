import flet as ft
from os import path

class Terminal(ft.UserControl):

    def __init__(self, uploads:object) -> None:
        super().__init__()
        self.uploads = uploads

    def build(self) -> ft.Card:

        save_btn = ft.ElevatedButton(
                text='сохранить',
                on_click=self.save_btn_clicked,
                )
        clear_btn = ft.ElevatedButton(
                text='очистить',
                on_click=self.clear_btn_clicked,
                )

        self.log_view = ft.ListView(
                auto_scroll=True,
                width=400, height=580,
                spacing=0,
                )

        terminal_view = ft.Card(
                elevation=3,
                width=420, height=670,
                content=ft.Container(
                    padding=ft.padding.only(
                        left=15, right=10, top=15, bottom=10),
                    content=ft.Column(
                        controls=[
                            self.log_view,
                            ft.Row(
                                controls=[
                                    save_btn,
                                    clear_btn,
                                    ]
                                ),
                            ]
                        ),
                    )
                )
        return terminal_view

    async def log_add(self, text:str|list) -> None:
        if isinstance(text, list):
            for row in text:
                self.log_view.controls.append(
                        ft.Text(
                            value=row,
                            )
                        )
            await self.log_view.update_async()
        
        elif isinstance(text, str):
            self.log_view.controls.append(
                    ft.Text(
                        value=text,
                        )
                    )
            await self.log_view.update_async()
        elif isinstance(text, int) or isinstance(text, float):
            self.log_view.controls.append(
                    ft.Text(
                        value=str(text),
                        )
                    )
            await self.log_view.update_async()
        else:
            print(f'text type: {type(text)}')
            raise TypeError

    async def save_btn_clicked(self, e) -> None:
        # log_len = len(self.log_view.controls)
        log_path = path.join(self.uploads.dpUnit1.path, 'логи.txt')
        with open(log_path, 'w') as fp:
            for item in self.log_view.controls:
                # write each item on a new line
                fp.write("%s\n" % item.value)
        await self.log_add(f'\n[*] Лог файл сохранен в:\n{log_path}')

    async def clear_btn_clicked(self, e) -> None:
        self.log_view.controls = []
        await self.log_view.update_async()
