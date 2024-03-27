import asyncio
import flet as ft

from utils.shared_memory import SharedMemory

class List(ft.UserControl):
    
    def __init__(self, label):
        super().__init__()
        self.units = []
        self.LABEL = label

        self.tbus_list = SharedMemory().tbus_list

    class Unit(ft.UserControl):
        def __init__(self, text:str, units_remove: callable):
            super().__init__()
            self.text = text
            self.units_remove = units_remove
        def build(self) -> ft.Row:
            label = ft.Text(
                    height=30, width=50, size=16,
                    value=self.text)
            btn_remove = ft.Container(
                    height=20, width=20, padding=0,
                    margin=ft.margin.only(right=7),
                    content=ft.Icon(
                        name=ft.icons.HIGHLIGHT_REMOVE_OUTLINED,
                        color=ft.colors.RED_200,
                        ),
                    on_click=self.btn_remove_unit_click,
                    # on_click=self.units_remove,
                    )
            unit = ft.Row(
                    expand=True,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        label,
                        btn_remove,
                        ])

            return unit
        async def btn_remove_unit_click(self, e) -> None:
            global units_view
            units_view.content.controls.remove(self)
            units_view.content.auto_scroll=False
            await units_view.update_async()
            units_view.content.auto_scroll=True
            self.units_remove(self.text)

    def build(self):

        class Input_control_unit(ft.UserControl):
            def __init__(self) -> None:
                super().__init__()
            def build(self) -> ft.TextField:
                unit = ft.TextField(
                    hint_text="#", content_padding=11,
                    height=35, width=35, bgcolor=ft.colors.WHITE,)
                return unit


        async def btn_add_unit_click(e)-> None:
            global units_view
            """ Parse wndws input and add unit. """
            async def input_error(wndws) -> None:
                """ Color wndws to RED. """
                for wndw in wndws:
                    # wndw.border = ft.InputBorder.OUTLINE
                    wndw.border_color = ft.colors.RED
                    wndw.border_width = 2
                    await wndw.update_async()
            async def empty_all_wndws(wndws) -> None:
                for wndw in wndws:
                    wndw.value = ""
                    await wndw.update_async()
            async def reset_input_error(wndws) -> None:
                for wndw in wndws:
                    wndw.border_color = ft.colors.BLACK
                    wndw.border_width = 1
                    await wndw.update_async()

            unit_number = ""
            wndws = [wndw1.controls[0],
                    wndw2.controls[0],
                    wndw3.controls[0],
                    wndw4.controls[0],
                    ]
            # Check that each wndw TextFiled has only one digit.
            if len(wndws[0].value) > 1 or len(wndws[1].value) > 1 \
                    or len(wndws[2].value) > 1 or len(wndws[3].value) > 1:
                await input_error(wndws)
                await empty_all_wndws(wndws)
                return
            # If all wndw TextField are empty - there is nothing to do.
            if len(wndws[0].value) == 0 and len(wndws[1].value) == 0 \
                    and len(wndws[2].value) == 0 and len(wndws[3].value) == 0:
                await empty_all_wndws(wndws)
                await reset_input_error(wndws)
                return
            # If there is some correct value in wndws.
            for wndw in wndws:
                # Check that value not empty
                if wndw.value:
                    # Check that can be converted in int
                    try:
                        int(wndw.value)
                        unit_number += wndw.value
                    except:
                        # It cant, so - incorrect input
                        await input_error(wndws)
                        await empty_all_wndws(wndws)
                        return
                else:
                    unit_number += '#'
            
            await empty_all_wndws(wndws)
            await reset_input_error(wndws)
            # if unit_number not in self.units:
            if unit_number not in self.tbus_list:
                unit = self.Unit(unit_number, self.remove_unit_from_units_list)
                units_view.content.controls.append(unit)
                await units_view.update_async()
                self.units.append(unit_number)
                self.tbus_list.append(unit_number)
            elif unit_number in self.tbus_list and unit_number not in self.units:
                # Unit is in other list and cannot be added into this list
                # Error color
                await input_error(wndws)
                await empty_all_wndws(wndws)


        wndw1 = Input_control_unit()
        wndw2 = Input_control_unit()
        wndw3 = Input_control_unit()
        wndw4 = Input_control_unit()
        btn_add_unit = ft.ElevatedButton(
                text=" ", icon=ft.icons.ADD,
                height=35, width=55, on_click=btn_add_unit_click,)
        
        input_view = ft.Row(
                controls=[
                    wndw1, wndw2, wndw3, wndw4, btn_add_unit,
                    ])

        global units_view
        units_view = ft.Container(
                bgcolor=ft.colors.WHITE,
                border=ft.border.all(1, ft.colors.BLACK87),
                border_radius=5,
                # alignment=ft.MainAxisAlignment.CENTER,
                content=ft.ListView(
                    height=75, width=175 + 55,
                    auto_scroll=True, padding=10,
                    )
                    
                )

        tbus_list_view = ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(value=self.LABEL),
                    input_view,
                    units_view,
                    ])
        
        return tbus_list_view

    # Create unit with pattern asociated.
    def remove_unit_from_units_list(self, unit:str) -> None:
        self.units.remove(unit)
        self.tbus_list.remove(unit)

    async def add_unit_from_ext(self, unit_number:str) -> None:
        global units_view
        unit = self.Unit(unit_number, self.remove_unit_from_units_list)
        # unit.units_remove = self.remove_unit_from_units_list
        units_view.content.controls.append(unit)
        await units_view.update_async()
        self.units.append(unit_number)
        self.tbus_list.append(unit_number)

