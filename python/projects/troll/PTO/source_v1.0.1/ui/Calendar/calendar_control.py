import asyncio
import flet as ft
from time import localtime as lt

from .calendar_title_control import Title_tile
from .day_control import Day
from .month_calendar import get_month_calendar

class Calendar(ft.UserControl):

    def __init__(self,) -> None:
        super().__init__()
        # Will be contain all month's days (working and weekends).
        self.days = []
        # Tile setup for 'Title_tile' and 'Day'
        # self.height reserved by 'UserControl' itself.
        self.uheight = 40
        self.uwidth = 40
        self.uborder_radius = 7
        self.umargin = -3
        self.ublur = 0
        self.grid_columns_numb = 7
        self.card_elevation = 3


    def build(self) -> ft.Card:
        
        # Week title
        self.title_view = ft.Row()
        for day in range(7):
            t = Title_tile(day,
                    self.uheight, self.uwidth, self.uborder_radius,
                    self.umargin, self.ublur)
            self.title_view.controls.append(t)

        # Grid of 'Day's.
        self.calendar_grid = ft.GridView(
            # How many columns should be
            runs_count=self.grid_columns_numb,
        )

        # Enclose 'calendar_grid' to 'calendar_view' Container
        # To be able to manipulate grid height and width
        self.calendar_view = ft.Container(
                height = 300,
                width = 300,
                content=self.calendar_grid,
                )

        self.date_view = ft.Text(size=18)

        # Init calendar grid.
        # Later it will be called to update 'calendar_grid'.
        date_now = lt()
        year = date_now.tm_year
        # we need next month, so add +1 to mon
        month = date_now.tm_mon + 1
        if month == 13:
            year += 1
            month = 1
        self.calendar_grid_update(month, year)

        # Final assemble of calendar Control
        self.main_view = ft.Card(
                elevation=self.card_elevation,
                content=ft.Container(
                    margin=7,
                    width=(self.uwidth + 2) * self.grid_columns_numb + 7,
                    height = 8 * self.uheight + 20,
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.END,
                        controls=[
                            self.date_view,
                            self.title_view,
                            self.calendar_view])
                    )
                )
        
        return self.main_view

    def calendar_grid_update(self, month:int, year:int) -> None:
        # Clear 'calendar_grid' controls
        try:
            # May cause exception on first startup
            self.calendar_grid.controls[0].non_working_days.clear()
            self.days.clear()
        except:
            pass
        self.calendar_grid.controls.clear()
        # Generate next month 'calendar_grid'

        # Create 'calendar_grid'.
        month_days = get_month_calendar(month, year)
        for week in month_days:
            for day in week:
                day_numb = day[0]
                day_lett = day[1]
                dday = Day(day_numb, day_lett,
                        self.uheight, self.uwidth,
                        self.uborder_radius, self.umargin, self.ublur)
                self.calendar_grid.controls.append(dday)
                if day_numb:
                    self.days.append(day_numb)

        # Month text
        match month:
            case 1: month_txt = 'Январь'
            case 2: month_txt = 'Февраль'
            case 3: month_txt = 'Март'
            case 4: month_txt = 'Апрель'
            case 5: month_txt = 'Май'
            case 6: month_txt = 'Июнь'
            case 7: month_txt = 'Июль'
            case 8: month_txt = 'Август'
            case 9: month_txt = 'Сентябрь'
            case 10: month_txt = 'Октябрь'
            case 11: month_txt = 'Ноябрь'
            case 12: month_txt = 'Декабрь'
            case _: month_txt = ''
        self.date_view.value=month_txt+' '+str(year)

    
    def get_non_working_days(self) -> list:
        """ Get list of non-working days. """
        result = self.calendar_grid.controls[0].non_working_days
        return result

    def get_working_days(self) -> list:
        """ Get list of working days. """
        non_working_days = self.get_non_working_days()
        working_days = [a for a in self.days if (a not in non_working_days)]
        # working_days = set(non_working_days).symmetric_difference(self.days)
        return working_days

    async def weekends_working_day(self, work: bool) -> None:
        """ Used by switch to change whether weekend are for work or not. """
        if work:
            for dday in self.calendar_grid.controls:
                await dday.weekends_work()
        else:
            for dday in self.calendar_grid.controls:
                await dday.weekends_dont_work()

