import asyncio
import flet as ft
from math import pi

from utils.primary_composer import Composer
from utils.egg import egg

class Start(ft.UserControl):

    def __init__(self, page,
            settings:object,
            calendar:object,
            uploads:object,
            terminal:object) -> None:
        super().__init__()
        self.page = page
        self.settings = settings
        self.calendar = calendar
        self.uploads = uploads
        self.terminal = terminal

    def build(self) -> ft.Card:

        async def btn_start_click(e) -> None:
            # Main algorithm
            self.btn_start.disabled=True
            await self.btn_start.update_async()
            self.btn_cancel.disabled=False
            await self.btn_cancel.update_async()

            await self.composer.start()

            # Reset to the beginning
            self.btn_start.disabled=False
            await self.btn_start.update_async()

            self.btn_cancel.disabled=True
            await self.btn_cancel.update_async()

        async def btn_cancel_click(e) -> None:
            self.btn_start.disabled=False
            await self.btn_start.update_async()
            self.btn_cancel.disabled=True
            await self.btn_cancel.update_async()

            await self.composer.stop()

        self.circle = ft.ProgressRing(
                bgcolor='#DDDDDD',
                color='#A076F9',
                stroke_width=10,
                width=110, height=110,
                # scale=ft.transform.Scale(3.0),
                # rotate=ft.transform.Rotate(pi/4),
                value=0.0,
                )


        self.btn_start = ft.ElevatedButton(
                text='НАЧАТЬ',
                width=110,
                style=ft.ButtonStyle(
                        bgcolor={
                            ft.MaterialState.DEFAULT: '#cbffa9',
                            ft.MaterialState.DISABLED: '#DDDDDD',
                        }),
                disabled=False,
                on_click=btn_start_click,
                )
        self.btn_cancel = ft.ElevatedButton(
                text='ОТМЕНА',
                style=ft.ButtonStyle(
                        bgcolor={
                            ft.MaterialState.DEFAULT: '#ff9b9b',
                            ft.MaterialState.DISABLED: '#DDDDDD',
                        }),
                width=110,
                disabled=True,
                on_click=btn_cancel_click,
                )

        self.composer = Composer(
                self.page,
                self.settings,
                self.calendar,
                self.uploads,
                self.terminal,
                self.circle,
                )
        
        start_view = ft.Card(
                elevation=3,
                width=478, height=298,
                content=ft.Container(
                    # gradient=ft.LinearGradient(
                    #     begin=ft.alignment.bottom_left,
                    #     end=ft.alignment.top_right,
                    #     colors=[
                    #         # '#EEEEEE',
                    #         # '#FFF1DC',
                    #         # '#E8D5C4',
                    #         # '#3A98B9',
                    #         ]
                    #     ),
                    # border_radius=12,

                    content=ft.Row(
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=50,
                        controls=[
                            self.circle,
                            ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=20,
                                controls=[
                                    self.btn_start,
                                    self.btn_cancel,
                                    ])
                            ])
                    )
        )


        # Black card
        # start_view = ft.Card(
        #         elevation=3,
        #         width=478, height=298,
        #         content=ft.Container(
        #             gradient=ft.LinearGradient(
        #                 begin=ft.alignment.bottom_left,
        #                 end=ft.alignment.top_right,
        #                 colors=[
        #                     '#1f2937',
        #                     '#111827']
        #                 ),
        #             border_radius=12,
        #             )
        #         )
        return start_view

