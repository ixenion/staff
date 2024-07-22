import flet as ft

class Day(ft.UserControl):
    """ Container with day number. """
    non_working_days = []

    def __init__(self, day_numb:int|str, day_lett:int,
            uheight:int,
            uwidth:int, uborder_radius:int, umargin:int, ublur:int) -> None:
        super().__init__()
        self.day_numb = day_numb
        self.day_lett = day_lett
        self.working_day = True
        # Color holidays in red
        if self.day_lett in [5, 6]:
            self.text_enb = ft.colors.RED
            self.text_dis = ft.colors.RED_100
            self.working_day = False
            self.non_working_append(self.day_numb)
        # Work days in black
        else:
            self.text_enb = ft.colors.BLACK87
            self.text_dis = ft.colors.BLACK26
        # View setup
        self.uheight = uheight
        self.uwidth = uwidth
        self.uborder_radius = uborder_radius
        self.umarging = umargin
        self.ublur = ublur

    def build(self) -> ft.Row:
        """ Container with day number. """
        # Text color depends on whether day is working or holly.
        label_color = self.text_enb if self.working_day else self.text_dis

        self.day_label = ft.Text(value=str(self.day_numb), color=label_color)
        self.day_view = ft.Container(
                height=self.uheight,
                width=self.uwidth,
                border_radius=self.uborder_radius,
                # padding from the 'Container' to the page.
                # '-3' because '0' isnt actually a zero.
                margin=self.umarging,
                # padding from day_label 'Text' inside to the 'Container'.
                # padding=10,
                # bgcolor=ft.colors.WHITE10,
                # blur=self.ublur,
                ink = True,
                
                on_click=self.day_on_click,

                alignment=ft.alignment.center,
                content=self.day_label)
        
        # If self.day_lett == 0 - this day not belongs to the current month;
        # Disable this day control:
        if not self.day_numb:
            self.day_view.content.value = ""
            self.day_view.disabled = True


        return ft.Row(controls=[self.day_view])

    async def day_on_click(self, e) -> None:
        await self.change_state()

    async def change_state(self) -> None:
        if self.working_day:
            # Disable day
            self.day_view.content.color = self.text_dis
            await self.day_view.update_async()
            # Fill in global variable 'working_days' to determine in future
            # what days in the month are working days.
            self.non_working_append(self.day_numb)
            self.working_day = False
        else:
            # Enable day
            self.day_view.content.color = self.text_enb
            await self.day_view.update_async()
            # Fill in global variable 'working_days' to determine in future
            # what days in the month are working days.
            try:
                """ List might not content value when switching from
                'Not work on weekend' to 'Work on weekend'. """
                self.non_working_days.remove(self.day_numb)
            except:
                pass
            self.working_day = True

    async def weekends_work(self) -> None:
        if self.day_lett in [5, 6]:
            self.day_view.content.color = self.text_enb
            await self.day_view.update_async()
            try:
                """ List might not content value when switching from
                'Not work on weekend' to 'Work on weekend'. """
                self.non_working_days.remove(self.day_numb)
            except:
                pass
            self.working_day = True
    async def weekends_dont_work(self) -> None:
        if self.day_lett in [5, 6]:
            self.day_view.content.color = self.text_dis
            await self.day_view.update_async()
            if self.day_numb not in self.non_working_days:
                self.non_working_append(self.day_numb)
            self.working_day = False

    def non_working_append(self, value) -> None:
        """ Main purpose is to avoid adding '0' to the list."""
        if value:
            self.non_working_days.append(value)
