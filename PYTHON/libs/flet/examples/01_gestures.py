import flet as ft

def main(page: ft.Page):

    def on_pan_update1(e: ft.DragUpdateEvent):
        c.top = max(0, c.top + e.delta_y)
        c.left = max(0, c.left + e.delta_x)
        c.update()

    def on_pan_update2(e: ft.DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.delta_y)
        e.control.left = max(0, e.control.left + e.delta_x)
        e.control.update()
    
    def on_double_tap(e: ft.DragUpdateEvent):
        print(f"on_double_tap")
        pass
    def on_double_tap_down(e: ft.DragUpdateEvent):
        print(f"on_double_tap_down")
        pass
    def on_scroll(e: ft.ScrollEvent):
        print(f"Scroll event detected")
        delta = 3
        c2.width = min(200, c2.width + delta if e.scroll_delta_y < 0 else c2.width - delta)
        c2.height = c2.width
        c2.update()
        pass

    gd = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=50,
        on_pan_update=on_pan_update1,
    )

    c = ft.Container(gd, bgcolor=ft.colors.AMBER, width=50, height=50, left=0, top=0)
    c2 = ft.Container(bgcolor=ft.colors.BLUE, width=50, height=50)

    gd1 = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=0,
        on_scroll=on_scroll,
        on_vertical_drag_update=on_pan_update2,
        on_double_tap=on_double_tap,
        on_double_tap_down=on_double_tap_down,
        left=100,
        top=100,
        content=c2,
    )

    page.add( ft.Stack([c, gd1], width=1000, height=500))

ft.app(target=main)
