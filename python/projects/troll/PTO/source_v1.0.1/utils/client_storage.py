from flet import Page

async def get_app_env(page:Page) -> dict:
    
    env_vars = {}

    # electro_tbus_list
    if await page.client_storage.contains_key_async("pto_electro_tbus_list"):
        pto_electro_tbus_list = await page.client_storage.get_async("pto_electro_tbus_list")
    else:
        pto_electro_tbus_list = []
    # lengthy_tbus_list
    if await page.client_storage.contains_key_async("pto_lengthy_tbus_list"):
        pto_lengthy_tbus_list = await page.client_storage.get_async("pto_lengthy_tbus_list")
    else:
        pto_lengthy_tbus_list = []
    # weekends_control_value
    if await page.client_storage.contains_key_async("pto_weekends_control_value"):
        pto_weekends_control_value = await page.client_storage.get_async("pto_weekends_control_value")
    else:
        pto_weekends_control_value = False
    # etbus_control_value
    if await page.client_storage.contains_key_async("pto_etbus_control_value"):
        pto_etbus_control_value = await page.client_storage.get_async("pto_etbus_control_value")
    else:
        pto_etbus_control_value = 2
    # ltbus_control_value
    if await page.client_storage.contains_key_async("pto_ltbus_control_value"):
        pto_ltbus_control_value = await page.client_storage.get_async("pto_ltbus_control_value")
    else:
        pto_ltbus_control_value = 1
    # all_ltbus_control_value
    if await page.client_storage.contains_key_async("pto_all_ltbus_control_value"):
        pto_all_ltbus_control_value = await page.client_storage.get_async("pto_all_ltbus_control_value")
    else:
        pto_all_ltbus_control_value = 5
    # alltbus_control_value
    if await page.client_storage.contains_key_async("pto_alltbus_control_value"):
        pto_alltbus_control_value = await page.client_storage.get_async("pto_alltbus_control_value")
    else:
        pto_alltbus_control_value = 5
    # pto_min_odometer
    if await page.client_storage.contains_key_async("pto_min_odometer_value"):
        pto_min_odometer_value = await page.client_storage.get_async("pto_min_odometer_value")
    else:
        pto_min_odometer_value = str(0)

    # file1_path
    if await page.client_storage.contains_key_async("pto_file1_path"):
        file1_path = await page.client_storage.get_async("pto_file1_path")
    else:
        file1_path = ""
    # file2_path
    if await page.client_storage.contains_key_async("pto_file2_path"):
        file2_path = await page.client_storage.get_async("pto_file2_path")
    else:
        file2_path = ""
    # file3_path
    if await page.client_storage.contains_key_async("pto_file3_path"):
        file3_path = await page.client_storage.get_async("pto_file3_path")
    else:
        file3_path = ""
    # file4_path
    if await page.client_storage.contains_key_async("pto_file4_path"):
        file4_path = await page.client_storage.get_async("pto_file4_path")
    else:
        file4_path = ""
    # dir1_path
    if await page.client_storage.contains_key_async("pto_dir1_path"):
        dir1_path = await page.client_storage.get_async("pto_dir1_path")
    else:
        dir1_path = ""

    env_vars['pto_electro_tbus_list'] = pto_electro_tbus_list
    env_vars['pto_lengthy_tbus_list'] = pto_lengthy_tbus_list
    env_vars['pto_weekends_control_value'] = pto_weekends_control_value
    env_vars['pto_etbus_control_value'] = pto_etbus_control_value
    env_vars['pto_ltbus_control_value'] = pto_ltbus_control_value
    env_vars['pto_all_ltbus_control_value'] = pto_all_ltbus_control_value
    env_vars['pto_alltbus_control_value'] = pto_alltbus_control_value
    env_vars['pto_min_odometer_value'] = pto_min_odometer_value

    env_vars['pto_file1_path'] = file1_path
    env_vars['pto_file2_path'] = file2_path
    env_vars['pto_file3_path'] = file3_path
    env_vars['pto_file4_path'] = file4_path
    env_vars['pto_dir1_path'] = dir1_path
    return env_vars

async def set_app_env(page: Page, env_vars:dict) -> None:
    
    for key in env_vars:
        await page.client_storage.set_async(key, env_vars[key])
