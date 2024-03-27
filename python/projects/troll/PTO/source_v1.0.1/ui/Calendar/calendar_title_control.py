import flet as ft

class Title_tile(ft.UserControl):
    """ Container with day number. """
    non_working_days = []

    def __init__(self, day:int,
            uheight, uwidth, uborder_radius,
            umargin, ublur) -> None:
        super().__init__()
        match day:
            case 0: txt = "Пн"
            case 1: txt = "Вт"
            case 2: txt = "Ср"
            case 3: txt = "Чт"
            case 4: txt = "Пт"
            case 5: txt = "Сб"
            case 6: txt = "Вс"
        self.label = txt
        # Color holidays in red
        if self.label in ["Сб", "Вс"]:
            self.text_enb = ft.colors.RED
        # Work days in black
        else:
            self.text_enb = ft.colors.BLACK87
        # View setup
        self.uheight = uheight
        self.uwidth = uwidth
        self.uborder_radius = uborder_radius
        self.umarging = umargin
        self.ublur = ublur

    def build(self) -> ft.Row:
        """ Container with day number. """
        # Text color depends on whether day is working or holly.
        label_color = self.text_enb

        self.day_label = ft.Text(value=self.label, color=label_color)
        self.day_view = ft.Container(
                height=self.uheight,
                width=self.uwidth,
                border_radius=self.uborder_radius,
                # padding from the 'Container' to the page.
                # '-3' because '0' isnt actually a zero.
                margin=self.umarging,
                # padding from day_label 'Text' inside to the 'Container'.
                # padding=10,
                bgcolor=ft.colors.WHITE10,
                # blur=self.ublur,
                disabled = True,

                alignment=ft.alignment.center,
                content=self.day_label)

        return ft.Row(controls=[self.day_view])
