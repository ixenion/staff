import flet as ft
from ui.Calendar.calendar_control import Calendar
from ui.Settings.settings_control import Settings
from ui.Uploads.uploads_control import Uploads
from ui.Start.start_control import Start
from ui.Terminal.terminal_control import Terminal

from utils.client_storage import get_app_env


async def main(page: ft.Page) -> None:

    # Load env varisbles
    env_vars = await get_app_env(page)

    # MAIN controls

    page.padding = -0
    page.window_width = 1400
    page.window_height = 750
    page.window_max_width = 1500
    page.window_max_height = 850
    page.title = 'Автоматизированное составление ежемесячного ТО'

    # page.rtl=True

    calendar = Calendar()

    settings = Settings(
            env_vars['pto_electro_tbus_list'],
            env_vars['pto_lengthy_tbus_list'],
            env_vars['pto_weekends_control_value'],
            env_vars['pto_etbus_control_value'],
            env_vars['pto_ltbus_control_value'],
            env_vars['pto_all_ltbus_control_value'],
            env_vars['pto_alltbus_control_value'],
            env_vars['pto_min_odometer_value'],
            calendar)
    
    uploads = Uploads(
            env_vars['pto_file1_path'],
            env_vars['pto_file2_path'],
            env_vars['pto_file3_path'],
            env_vars['pto_file4_path'],
            env_vars['pto_dir1_path'],
            )

    terminal = Terminal(
            uploads,
            )
    start_menu = Start(
            page,
            settings,
            calendar,
            uploads,
            terminal,
            )

    controls_view = ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                settings,
                                calendar,
                            ]
                        ),
                        ft.Row(
                            controls=[
                                uploads,
                                start_menu,
                            ]
                        ),
                    ]
                ),
                terminal,
            ]
        )

    main_view = ft.Container(
            padding=40,
            gradient=ft.LinearGradient(
                begin=ft.alignment.bottom_left,
                end=ft.alignment.top_right,
                colors=[
                    '#FFF1DC',
                    '#E8D5C4',
                    '#3A98B9',
                    # '#CDF0EA',
                    # '#C490E4',
                    ],
                ),
            content=controls_view,
            )

    await page.add_async(main_view)

ft.app(target=main)
# ft.app(target=main, view=ft.WEB_BROWSER, port=8080)
