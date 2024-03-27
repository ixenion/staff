import asyncio
import flet as ft
from time import localtime as lt

from .etbus_list_view import List as elist
from .ltbus_list_view import List as llist


class Settings(ft.UserControl):
    """ Settings UI control.
        Includes:
        1. electro_tbus_list_view (...),
        2. lengthy_tbus_list_view (...),
        3. date_view (year_control, month_control, weekends_control, day_control),
        4. tbus_sett_view (...).
    """

    def __init__(
            self,
            # 'year', 'month', 'day' uses their own algorithms,
            electro_tbus_list, lengthy_tbus_list,
            weekends_control_value,
            etbus_control_value, ltbus_control_value,
            all_ltbus_control_value,
            alltbus_control_value, min_odometer_value,
            calendar: object) -> None:
        super().__init__()
        self.calendar = calendar

        self.electro_tbus_list = electro_tbus_list
        self.lengthy_tbus_list = lengthy_tbus_list
        self.weekends_control_value = weekends_control_value
        self.etbus_control_value = etbus_control_value
        self.ltbus_control_value = ltbus_control_value
        self.all_ltbus_control_value = all_ltbus_control_value
        self.alltbus_control_value = alltbus_control_value
        self.min_odometer_value = min_odometer_value


    def build(self) -> ft.Card:
        
        # ------------------------------------------------------------------#
        # ELECTRO TROLLEYBUS LIST VIEW (electro_tbus_list_view)
        
        self.electro_tbus_list_view = elist("Электробусы")
        loop = asyncio.get_event_loop()
        for unit_number in self.electro_tbus_list:
            loop.create_task(self.electro_tbus_list_view.add_unit_from_ext(unit_number))


        # ------------------------------------------------------------------#
        # LENGTHY TROLLEYBUS LIST VIEW (lengthy_tbus_list_view)

        self.lengthy_tbus_list_view = llist("Гармошки")
        for unit_number in self.lengthy_tbus_list:
            loop.create_task(self.lengthy_tbus_list_view.add_unit_from_ext(unit_number))

        # ------------------------------------------------------------------#
        # DATE VIEW (date_view)

        date_now = lt()
        year = date_now.tm_year
        month = date_now.tm_mon + 1
        day = date_now.tm_mday
        if month == 13:
            year += 1
            month = 1

        self.year_control = ft.TextField(
                bgcolor=ft.colors.WHITE,
                on_change=self.year_change,
                label="Год", value=str(year), dense=True,
                width=125, height=45, icon=ft.icons.AREA_CHART_ROUNDED)
        self.month_control = ft.TextField(
                on_change=self.month_change,
                bgcolor=ft.colors.WHITE,
                label="Месяц", value=str(month), dense=True,
                width=125, height=45, icon=ft.icons.CALENDAR_MONTH)
        self.day_control = ft.TextField(
                on_change=self.day_change,
                bgcolor=ft.colors.WHITE,
                label="День (TO2)", value=day,  dense=True,
                width=125, height=45, icon=ft.icons.ADS_CLICK_OUTLINED)
        if self.weekends_control_value:
            loop = asyncio.get_event_loop()
            loop.create_task(self.switch_weekends('e'))
        self.weekends_control = ft.Row(
                alignment=ft.MainAxisAlignment.START,
                spacing=14.,
                controls=[
                    ft.Container(
                        margin=-12,
                        content=ft.IconButton(
                            icon=ft.icons.ICECREAM_ROUNDED,
                            # icon=ft.icons.WEEKEND_OUTLINED,
                            icon_size=25,)
                        ),
                    ft.Switch(label="Вых.", value=self.weekends_control_value,
                        on_change=self.switch_weekends,
                        label_position=ft.LabelPosition.RIGHT),
                        
                    ]
                )

        date_view = ft.Row(
                [
                    ft.Column([
                        self.year_control,
                        self.month_control,
                    ]),
                    ft.Column([
                        self.weekends_control,
                        self.day_control,
                    ])
                ]
            )

        # ------------------------------------------------------------------#
        # TROLLEYBUS SETTINGS VIEW (tbus_set_view)

        self.placeholder = ft.Container(
                width=125, height=45,)
        self.etbus_control = ft.TextField(
                on_change=self.etbus_control_change,
                bgcolor=ft.colors.WHITE,
                label="Элктр/дн", value=self.etbus_control_value, dense=True,
                width=125, height=45, icon=ft.icons.BATTERY_CHARGING_FULL_ROUNDED)
        self.ltbus_control = ft.TextField(
                on_change=self.ltbus_control_change,
                bgcolor=ft.colors.WHITE,
                label="Грмшк/дн", value=self.ltbus_control_value, dense=True,
                width=125, height=45, icon=ft.icons.LINK_OUTLINED)

        self.all_ltbus_control = ft.TextField(
                on_change=self.all_ltbus_control_change,
                bgcolor=ft.colors.WHITE,
                label="ВсгСгр/дн", value=self.all_ltbus_control_value, dense=True,
                width=125, height=45, icon=ft.icons.AUTO_AWESOME_MOTION_OUTLINED)
        self.alltbus_control = ft.TextField(
                on_change=self.alltbus_control_change,
                bgcolor=ft.colors.WHITE,
                label="Всего/дн", value=self.alltbus_control_value, dense=True,
                width=125, height=45, icon=ft.icons.AUTO_AWESOME_MOTION_ROUNDED)
        self.min_odometer = ft.TextField(
                on_change=self.min_odometer_change,
                bgcolor=ft.colors.WHITE,
                label="Мин. км.", value=self.min_odometer_value, dense=True,
                width=125, height=45,
                icon=ft.icons.AIRLINE_STOPS_OUTLINED,)
                # icon=ft.icons.LINEAR_SCALE_OUTLINED,)

        tbus_set_view = ft.Row(
                [
                    ft.Column([
                        self.placeholder,
                        self.etbus_control,
                        self.ltbus_control,
                    ]),
                    ft.Column([
                        self.all_ltbus_control,
                        self.alltbus_control,
                        self.min_odometer,
                    ])
                ]
            )

        
        
        # MAIN view

        settings_view = ft.Card(
                elevation=3,
                content=ft.Container(
                    width=505,
                    margin=20,
                    content=ft.Column(
                        [   
                            ft.Row(
                                vertical_alignment = ft.CrossAxisAlignment.END,
                                controls=[
                                self.electro_tbus_list_view,
                                date_view,
                                ]
                                ),
                            ft.Row(
                                vertical_alignment = ft.CrossAxisAlignment.END,
                                controls=[
                                self.lengthy_tbus_list_view,
                                tbus_set_view,
                                ]),
                            ]
                        )
                    )
                )


        return settings_view

        # functions
        
    async def switch_weekends(self, e) -> None:
        if self.weekends_control.controls[1].value:
            await self.calendar.weekends_working_day(1)
            self.weekends_control.controls[0].content.icon=ft.icons.ROCKET_LAUNCH_ROUNDED
            # self.weekends_control.controls[0].content.icon=ft.icons.CLOUD_OFF_ROUNDED
            await self.weekends_control.update_async()
            self.weekends_control_value = True
            return
        await self.calendar.weekends_working_day(0)
        self.weekends_control.controls[0].content.icon=ft.icons.ICECREAM_ROUNDED
        await self.weekends_control.update_async()
        self.weekends_control_value = False

    async def year_change(self, e) -> None:
        try:
            # Check that year_control value is int
            int(self.year_control.value)
        except:
            self.year_control.border_color = ft.colors.RED
            self.year_control.border_width = 2
            await self.year_control.update_async()
            return
        if len(self.year_control.value) == 4:
            self.year_control.border_color = ft.colors.BLACK
            self.year_control.border_width = 1
            await self.year_control.update_async()
            self.calendar.calendar_grid_update(
                int(self.month_control.value), int(self.year_control.value))
            # Update calendar grid
            await self.calendar.update_async()
            # Restore weekends value in calendar grid
            if self.weekends_control_value:
                await self.calendar.weekends_working_day(1)
            return
        self.year_control.border_color = ft.colors.RED
        self.year_control.border_width = 2
        await self.year_control.update_async()

    async def month_change(self, e) -> None:
        try:
            # Check that year_control value is int
            int(self.month_control.value)
        except:
            self.month_control.border_color = ft.colors.RED
            self.month_control.border_width = 2
            await self.month_control.update_async()
            return

        if 12 >= int(self.month_control.value) > 0:
            self.month_control.border_color = ft.colors.BLACK
            self.month_control.border_width = 1
            await self.month_control.update_async()
            # Update calendar Grid
            self.calendar.calendar_grid_update(
                    int(self.month_control.value), int(self.year_control.value))
            # Update calendar grid
            await self.calendar.update_async()
            # Restore weekends value in calendar grid
            if self.weekends_control_value:
                await self.calendar.weekends_working_day(1)
            return
        self.month_control.border_color = ft.colors.RED
        self.month_control.border_width = 2
        await self.month_control.update_async()

    async def day_change(self, e) -> None:
        try:
            int(self.day_control.value)
        except:
            self.day_control.border_color = ft.colors.RED
            self.day_control.border_width = 2
            await self.day_control.update_async()
            return
        if 31 >= int(self.day_control.value) > 0:
            self.day_control.border_color = ft.colors.BLACK
            self.day_control.border_width = 1
            await self.day_control.update_async()
            return
        self.day_control.border_color = ft.colors.RED
        self.day_control.border_width = 2
        await self.day_control.update_async()


    async def etbus_control_change(self, e) -> None:
        try:
            int(self.etbus_control.value)
        except:
            self.etbus_control.border_color = ft.colors.RED
            self.etbus_control.border_width = 2
            await self.etbus_control.update_async()
            return
        if len(self.etbus_control.value) > 0:
            self.etbus_control.border_color = ft.colors.BLACK
            self.etbus_control.border_width = 1
            await self.etbus_control.update_async()
            return
        self.etbus_control.border_color = ft.colors.RED
        self.etbus_control.border_width = 2
        await self.etbus_control.update_async()

    async def ltbus_control_change(self, e) -> None:
        try:
            int(self.ltbus_control.value)
        except:
            self.ltbus_control.border_color = ft.colors.RED
            self.ltbus_control.border_width = 2
            await self.ltbus_control.update_async()
            return
        if len(self.ltbus_control.value) > 0:
            self.ltbus_control.border_color = ft.colors.BLACK
            self.ltbus_control.border_width = 1
            await self.ltbus_control.update_async()
            return
        self.ltbus_control.border_color = ft.colors.RED
        self.ltbus_control.border_width = 2
        await self.ltbus_control.update_async()

    async def all_ltbus_control_change(self, e) -> None:
        try:
            float(self.all_ltbus_control.value)
        except:
            self.all_ltbus_control.border_color = ft.colors.RED
            self.all_ltbus_control.border_width = 2
            await self.all_ltbus_control.update_async()
            return
        if len(self.all_ltbus_control.value) > 0:
            self.all_ltbus_control.border_color = ft.colors.BLACK
            self.all_ltbus_control.border_width = 1
            await self.all_ltbus_control.update_async()
            return
        self.all_ltbus_control.border_color = ft.colors.RED
        self.all_ltbus_control.border_width = 2
        await self.all_ltbus_control.update_async()

    async def alltbus_control_change(self, e) -> None:
        try:
            float(self.alltbus_control.value)
        except:
            self.alltbus_control.border_color = ft.colors.RED
            self.alltbus_control.border_width = 2
            await self.alltbus_control.update_async()
            return
        if len(self.alltbus_control.value) > 0:
            self.alltbus_control.border_color = ft.colors.BLACK
            self.alltbus_control.border_width = 1
            await self.alltbus_control.update_async()
            return
        self.alltbus_control.border_color = ft.colors.RED
        self.alltbus_control.border_width = 2
        await self.alltbus_control.update_async()

    async def min_odometer_change(self, e) -> None:
        try:
            int(self.min_odometer.value)
        except:
            self.min_odometer.border_color = ft.colors.RED
            self.min_odometer.border_width = 2
            await self.min_odometer.update_async()
            return
        if len(self.min_odometer.value) > 0:
            self.min_odometer.border_color = ft.colors.BLACK
            self.min_odometer.border_width = 1
            await self.min_odometer.update_async()
            return
        self.min_odometer.border_color = ft.colors.RED
        self.min_odometer.border_width = 2
        await self.min_odometer.update_async()

    # In case etbus from ext is broken
    async def init(self) -> None:
        loop = asyncio.get_event_loop()
        for unit_number in self.electro_tbus_list:
            loop.create_task(self.electro_tbus_list_view.add_unit_from_ext(unit_number))
        for unit_number in self.lengthy_tbus_list:
            loop.create_task(self.lengthy_tbus_list_view.add_unit_from_ext(unit_number))

