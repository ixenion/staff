import flet as ft

class Uploads(ft.UserControl):

    def __init__(self,
            file1_path:str, file2_path:str,
            file3_path:str, file4_path:str,
            dir1_path:str,):
        super().__init__()
        self.file1_path = file1_path
        self.file2_path = file2_path
        self.file3_path = file3_path
        self.file4_path = file4_path
        self.dir1_path = dir1_path
        

    def build(self) -> ft.Card:
        
        class FilePickerUnit(ft.UserControl):
            def __init__(self, path:str, btn_text:str):
                super().__init__()
                self.btn_text = btn_text
                self.path = path

            def build(self) -> ft.Row:

                path = ft.Text(
                        value=self.path,
                        size=16,
                        text_align=ft.TextAlign.RIGHT,
                        selectable=True, no_wrap=True,
                        )

                text_view = ft.Container(
                        bgcolor=ft.colors.WHITE,
                        border=ft.border.all(1, ft.colors.BLACK),
                        border_radius=5,
                        padding=ft.padding.all(4),

                        content=ft.ListView(
                            auto_scroll=True,
                            height=27, width=240,
                            horizontal=True,
                            controls=[
                                path,
                                ],
                            )
                        )

                # Pick files dialog
                async def pick_file_result(e: ft.FilePickerResultEvent):
                    path.value = e.files[0].path if e.files != None else ""
                    await path.update_async()
                    self.path = path.value
                pick_file_dialog = ft.FilePicker(on_result=pick_file_result)

                file_upload_btn = ft.ElevatedButton(
                        width=90,
                        text=self.btn_text,
                        # icon=ft.icons.ADD_CIRCLE_ROUNDED,
                        on_click=pick_file_dialog.pick_files_async,
                        )
                
                filePickerUnit = ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            pick_file_dialog,
                            text_view,
                            file_upload_btn,
                            ])
                return filePickerUnit

        class DirPickerUnit(ft.UserControl):
            def __init__(self, path:str, btn_text:str):
                super().__init__()
                self.btn_text = btn_text
                self.path = path

            def build(self) -> ft.Row:

                path = ft.Text(
                        value=self.path,
                        size=16,
                        text_align=ft.TextAlign.RIGHT,
                        selectable=True, no_wrap=True,
                        )

                text_view = ft.Container(
                        bgcolor=ft.colors.WHITE,
                        border=ft.border.all(1, ft.colors.BLACK),
                        border_radius=5,
                        padding=ft.padding.all(4),

                        content=ft.ListView(
                            auto_scroll=True,
                            height=27, width=240,
                            horizontal=True,
                            controls=[
                                path,
                                ],
                            )
                        )

                # Pick directory dialog
                async def get_directory_result(e: ft.FilePickerResultEvent):
                    path.value = e.path if e.path else ""
                    await path.update_async()
                    # Check that path not empty
                    # (Cant change container border color)
                    self.path = path.value

                get_directory_dialog = ft.FilePicker(on_result=get_directory_result)

                file_upload_btn = ft.ElevatedButton(
                        width=90,
                        text=self.btn_text,
                        # icon=ft.icons.ADD_CIRCLE_ROUNDED,
                        on_click=get_directory_dialog.get_directory_path_async,
                        )
                
                dirPickerUnit = ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            get_directory_dialog,
                            text_view,
                            file_upload_btn,
                            ])
                return dirPickerUnit


        self.fpUnit1 = FilePickerUnit(path=self.file1_path, btn_text="1C")
        self.fpUnit2 = FilePickerUnit(path=self.file2_path, btn_text="TO1")
        self.fpUnit3 = FilePickerUnit(path=self.file3_path, btn_text="TO2")
        self.fpUnit4 = FilePickerUnit(path=self.file4_path, btn_text="ИСКЛ")
        self.dpUnit1 = DirPickerUnit(path=self.dir1_path, btn_text="ввд")

        self.upload_control_view = ft.Card(
                elevation=3,
                content=ft.Container(
                    # width=505,
                    width=350, height=250,
                    margin=20,
                    content=ft.Column(
                        spacing=7,
                        controls=[
                            self.fpUnit1,
                            self.fpUnit2,
                            self.fpUnit3,
                            self.fpUnit4,
                            ft.Divider(),
                            self.dpUnit1,
                        ]
                    )

                ),
            )
        return self.upload_control_view
