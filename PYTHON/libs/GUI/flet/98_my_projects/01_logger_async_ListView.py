import asyncio
import flet as ft
from time import time

async def main(page: ft.Page):

    async def payload():
        """ Simulates log generation.
        Generates UNIX timestamp once at every second."""
        while True:
            lv.controls.append(ft.Text(f"{round(time())}", color="#72b01d"))
            await lv.update_async()
            await asyncio.sleep(1)

    async def add_btn_click(e):
        """ Add text button handler.
        Adds text to ListView."""
        lv.controls.append(ft.Text(f"sup", color="#72b01d"))
        await lv.update_async()

    async def clr_btn_click(e):
        """ Clear button handler.
        Clears ListView content."""
        lv.controls = None
        await lv.update_async()

    async def switch1_change(e):
        lv.auto_scroll = switch1.value
        lv.controls.append(ft.Text(f"Autoscroll: {switch1.value}", color="#72b01d"))
        await lv.update_async()

    # UI setup
    add_btn = ft.FilledButton(text="Add text", icon=ft.icons.ADD, width=130, on_click=add_btn_click)
    add_btn.bgcolor="#72b01d"
    clr_btn = ft.FilledButton(text="Clear", icon=ft.icons.CLEAR, width=130, on_click=clr_btn_click)
    clr_btn.bgcolor="#72b01d"
    switch1 = ft.Switch(label="Autoscroll", value=True, on_change=switch1_change, )
    switch1.active_track_color="#72b01d"
    switch1.thumb_color={
        ft.MaterialState.HOVERED: "#adb5bd",
        ft.MaterialState.FOCUSED: ft.colors.RED,
        ft.MaterialState.DEFAULT: "#ced4da",
    }
    # padding here means padding from ft.ListView to ft.Container
    lv = ft.ListView(expand=True, spacing=0, padding=5, auto_scroll=True)
    container1 = ft.Container(
            lv,
            width=300,
            height=600,
            alignment=ft.alignment.center,
            bgcolor= "#343a40",
            border=ft.border.all(1, "#343a40"),
            border_radius=ft.border_radius.all(5)
    )

    # Page setup
    page.window_height = 650
    page.window_width = 500
    page.bgcolor = "#495057"

    # main
    loop = asyncio.get_event_loop()
    await page.add_async(
            ft.Row(controls=[
                container1,
                ft.Column(controls=[
                    add_btn,
                    clr_btn,
                    switch1
                    ])
                ])
            )
    loop.create_task(payload())

ft.app(target=main)
