import asyncio
from datetime import datetime
import traceback
from os import path

from .client_storage import set_app_env
from .input_file_processer import InputFileProcesser
from .main_processer import MainProcesser
from .egg import egg
from .egg_text import kitty_text
from .egg_text import kitty_text2

class Composer:

    def __init__(self, page,
            settings:object,
            calendar:object,
            uploads:object,
            terminal:object,
            circle_view) -> None:
        self.page = page
        self.settings = settings
        self.calendar = calendar
        self.uploads = uploads
        self.terminal = terminal
        self.progress_view = circle_view

    async def start(self) -> None:

        # Easter egg
        async def check_for_egg(settings:object) -> str:
            # year = int(settings.year_control.value)
            year = settings.year_control.value
            text = egg(year)
            await self.terminal.log_add(text)
            return text
        if await check_for_egg(self.settings):
            return


        async def main() -> None:

            # Log all input params
            await self.terminal.log_add(f'\n{datetime.now()}\n[*] Проверка параметров настройки...\n')

            env_vars = await self.gather_all_vars(self.settings, self.uploads)
            await set_app_env(self.page, env_vars)
        
            for key in env_vars:
                line_txt = f'{key}: {env_vars[key]}'
                await self.terminal.log_add(line_txt)
            # await self.terminal.log_add('\n')
            
            # Check that all variables are correct
            if not await self.check_env_vars(env_vars):
                await self.terminal.log_add('[-] ОШИБКА: неверные параметры настройки.\n')
                self.progress_view.value = 1.0
                self.progress_view.color = '#F0DE36'
                await self.progress_view.update_async()
                return

            # MAIN
            await self.terminal.log_add(f'\n[*] Проверка параметров настройки успешно завершена.\n')
            # reset progress_ring
            self.progress_view.value = 0
            self.progress_view.color = '#A076F9'
            await self.progress_view.update_async()
            # Start main file processer function
            input_file_processer = InputFileProcesser(
                    # env_vars,
                    self.settings,
                    self.calendar,
                    self.uploads,
                    self.progress_view,
                    self.terminal)
            all_units, exceptions, file_to1, file_to1_meta = await input_file_processer.start()
            # await main_file_processer.start_test_payload()
            main_processer = MainProcesser(
                    env_vars,
                    self.uploads,
                    self.progress_view,
                    self.terminal,
                    all_units,
                    exceptions,
                    file_to1,
                    file_to1_meta,
                    )
            await main_processer.start()

            # Clear memory
            del all_units
            del exceptions
            del file_to1
            del file_to1_meta

            # Task completed
            # await asyncio.sleep(0.5)
            await self.terminal.log_add(f'\n{datetime.now()}\n[+] УСПЕШНО.')
            await asyncio.sleep(0.1)
            await self.terminal.log_add(kitty_text())
            self.progress_view.value = 1.0
            self.progress_view.color = '#A2FF86'
            await self.progress_view.update_async()


        self.main_task = asyncio.create_task(main())

        # Redirrect all exception messages to the terminal_view
        try:
            await self.main_task
        except Exception as e:
            await self.terminal.log_add(f'\n{datetime.now()}\n[-] ОШИБКА алгоритма:\n')
            exc_list = traceback.format_exception(e)
            for exception_str in exc_list:
                await self.terminal.log_add(f'{exception_str}')
            self.progress_view.color = '#FF6D60'
            if not self.progress_view.value:
                self.progress_view.value = 1.0
            await self.progress_view.update_async()
            # Add kitty_text_2
            await self.terminal.log_add(kitty_text2())
            return

    async def stop(self) -> None:
        self.main_task.cancel()
        await self.terminal.log_add(f'\n{datetime.now()}\n[-] ОТМЕНЕНО.')
        self.progress_view.color = '#FF6D60'
        await self.progress_view.update_async()

    
    async def check_env_vars(self, env_vars:dict) -> bool:
        # Check that all parameters are correct
        check_result = True

        # No need to check
        # env_vars['pto_electro_tbus_list']
        # env_vars['pto_lengthy_tbus_list']
        # env_vars['pto_weekends_control_value']
        # YEAR
        try:
            pto_year = int(env_vars['pto_year'])
            if len(str(pto_year)) != 4:
                check_result = False
                await self.terminal.log_add(f'[-] Неверное значение ГОДА: "{pto_year}"')
                await self.terminal.log_add(f'    Должно быть целым четырехзначным числом.\n')
        except:
            check_result = False
            await self.terminal.log_add(f"[-] Неверное значение ГОДА: '{env_vars['pto_year']}'")
            await self.terminal.log_add(f'    Должно быть целым четырехзначным числом.\n')
        # MONTH
        try:
            pto_month = int(env_vars['pto_month'])
            if not 13 > pto_month > 0:
                check_result = False
                await self.terminal.log_add(f'[-] Неверное значение МЕСЯЦА: "{pto_month}"')
                await self.terminal.log_add(f'    Должно быть целочисленным в интервале от 1 до 12.\n')
        except:
            check_result = False
            await self.terminal.log_add(f"[-] Неверное значение МЕСЯЦА: '{env_vars['pto_month']}'")
            await self.terminal.log_add(f'    Должно быть целочисленным в интервале от 1 до 12.\n')
        # DAY
        try:
            pto_day = int(env_vars['pto_day'])
            if not 32 > pto_day > 0:
                check_result = False
                await self.terminal.log_add(f'[-] Неверное значение ДНЯ: "{pto_day}"')
                await self.terminal.log_add(f'    Должно быть целочисленным в интервале от 1 до 31.\n')
        except:
            check_result = False
            await self.terminal.log_add(f"[-] Неверное значение ДНЯ: '{env_vars['pto_day']}'")
            await self.terminal.log_add(f'    Должно быть целочисленным в интервале от 1 до 31.\n')
        # WORKING DAYs
        if len(env_vars['working_days_list']) == 0 and \
                len(env_vars['non_working_days_list']) == 0:
            check_result = False
            await self.terminal.log_add(f'[-] Неверное значение КАЛЕНДАРЯ.')
            await self.terminal.log_add(f'    Должен быть хотя бы один рабочий день.\n')
        # ETBUS NUM
        try:
            pto_etbus_control_value = int(env_vars['pto_etbus_control_value'])
            if not pto_etbus_control_value > 0:
                check_result = False
                await self.terminal.log_add(f'[-] Неверное значение Електр/дн: "{pto_etbus_control_value}"')
                await self.terminal.log_add(f'    Должно быть неотрицательным целочисленным.\n')
        except:
            check_result = False
            await self.terminal.log_add(f"[-] Неверное значение Електр/дн: '{env_vars['pto_etbus_control_value']}'")
            await self.terminal.log_add(f'    Должно быть неотрицательным целочисленным.\n')
        # LTBUS NUM
        try:
            pto_ltbus_control_value = int(env_vars['pto_ltbus_control_value'])
            if not pto_ltbus_control_value > 0:
                check_result = False
                await self.terminal.log_add(f'[-] Неверное значение Грмшк/дн: "{pto_ltbus_control_value}"')
                await self.terminal.log_add(f'    Должно быть неотрицательным целочисленным.\n')
        except:
            check_result = False
            await self.terminal.log_add(f"[-] Неверное значение Грмшк/дн: '{env_vars['pto_ltbus_control_value']}'")
            await self.terminal.log_add(f'    Должно быть неотрицательным целочисленным.\n')
        # ALL_LTBUS NUM
        try:
            pto_all_ltbus_control_value = float(env_vars['pto_all_ltbus_control_value'])
            if not pto_all_ltbus_control_value > 0:
                check_result = False
                await self.terminal.log_add(f'[-] Неверное значение Всг Гр/дн: "{pto_all_ltbus_control_value}"')
                await self.terminal.log_add(f'    Должно быть неотрицательным рациональным.\n')
        except:
            check_result = False
            await self.terminal.log_add(f"[-] Неверное значение Всг Гр/дн: '{env_vars['pto_all_ltbus_control_value']}'")
            await self.terminal.log_add(f'    Должно быть неотрицательным рациональным.\n')
        # ALLTBUS NUM
        try:
            pto_alltbus_control_value = float(env_vars['pto_alltbus_control_value'])
            if not pto_alltbus_control_value > 0:
                check_result = False
                await self.terminal.log_add(f'[-] Неверное значение Всего/дн: "{pto_alltbus_control_value}"')
                await self.terminal.log_add(f'    Должно быть неотрицательным целочисленным.\n')
        except:
            check_result = False
            await self.terminal.log_add(f"[-] Неверное значение Всего/дн: '{env_vars['pto_alltbus_control_value']}'")
            await self.terminal.log_add(f'    Должно быть неотрицательным целочисленным.\n')
        # MIN ODOMETER
        try:
            pto_min_odometer_value = int(env_vars['pto_min_odometer_value'])
            if not pto_min_odometer_value >= 0:
                check_result = False
                await self.terminal.log_add(f'[-] Неверное значение Мин. км.: "{pto_min_odometer_value}"')
                await self.terminal.log_add(f'    Должно быть неотрицательным целочисленным.\n')
        except:
            check_result = False
            await self.terminal.log_add(f"[-] Неверное значение Мин. км.: '{env_vars['pto_min_odometer_value']}'")
            await self.terminal.log_add(f'    Должно быть неотрицательным целочисленным.\n')
        # FILE1 FIELD
        path1 = env_vars['pto_file1_path']
        if path1 == "" or not path.exists(path1):
            check_result = False
            await self.terminal.log_add(f'[-] Неверный путь к файлу 1С.\n')
        # FILE2 FIELD
        path2 = env_vars['pto_file2_path']
        if path2 == "" or not path.exists(path2):
            check_result = False
            await self.terminal.log_add(f'[-] Неверный путь к файлу TO1.\n')
        # FILE3 FIELD
        path3 = env_vars['pto_file3_path']
        if path3 == "" or not path.exists(path3):
            check_result = False
            await self.terminal.log_add(f'[-] Неверный путь к файлу TO2.\n')
        # FILE4 FIELD ( separate exceptions file)
        # Make this parameter not optional (?)
        path4 = env_vars['pto_file4_path']
        if path4 == "" or not path.exists(path4):
            # check_result = False
            # await self.terminal.log_add(f'[✘] Неверный путь к файлу исключений.\n')
            await self.terminal.log_add(f'[!] ВНИМАНИЕ: файл с исключениями отсутствует.\n')
        # DIR1 FIELD
        dir1 = env_vars['pto_dir1_path']
        if dir1 == "" or not path.exists(dir1):
            check_result = False
            await self.terminal.log_add(f'[-] Неверный путь к папке для итоговых файлов.\n')

        return check_result

    async def gather_all_vars(self,
            settings: object,
            uploads: object) -> dict:

        env_vars = {}

        pto_electro_tbus_list = settings.electro_tbus_list_view.units
        pto_lengthy_tbus_list = settings.lengthy_tbus_list_view.units
        pto_weekends_control_value = settings.weekends_control.controls[1].value
        pto_etbus_control_value = settings.etbus_control.value
        pto_ltbus_control_value = settings.ltbus_control.value
        pto_all_ltbus_control_value = settings.all_ltbus_control.value
        pto_alltbus_control_value = settings.alltbus_control.value
        pto_min_odometer_value = settings.min_odometer.value

        pto_file1_path = uploads.fpUnit1.path
        pto_file2_path = uploads.fpUnit2.path
        pto_file3_path = uploads.fpUnit3.path
        pto_file4_path = uploads.fpUnit4.path
        pto_dir1_path = uploads.dpUnit1.path

        env_vars['pto_electro_tbus_list'] = pto_electro_tbus_list
        env_vars['pto_lengthy_tbus_list'] = pto_lengthy_tbus_list
        env_vars['pto_year'] = settings.year_control.value
        env_vars['pto_month'] = settings.month_control.value
        env_vars['pto_day'] = settings.day_control.value
        env_vars['pto_weekends_control_value'] = pto_weekends_control_value
        env_vars['working_days_list'] = self.calendar.get_working_days()
        env_vars['non_working_days_list'] = self.calendar.get_non_working_days()

        env_vars['pto_etbus_control_value'] = pto_etbus_control_value
        env_vars['pto_ltbus_control_value'] = pto_ltbus_control_value
        env_vars['pto_all_ltbus_control_value'] = pto_all_ltbus_control_value
        env_vars['pto_alltbus_control_value'] = pto_alltbus_control_value
        env_vars['pto_min_odometer_value'] = pto_min_odometer_value
        env_vars['pto_file1_path'] = pto_file1_path
        env_vars['pto_file2_path'] = pto_file2_path
        env_vars['pto_file3_path'] = pto_file3_path
        env_vars['pto_file4_path'] = pto_file4_path
        env_vars['pto_dir1_path'] = pto_dir1_path

        return env_vars

