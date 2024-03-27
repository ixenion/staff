import flet as ft

def main(page):

    def add_clicked(e):
        # check that 'new_task.value' is empty:
        if not new_task.value:
            page.snack_bar = ft.SnackBar(ft.Text(f"[!] Empty task."))
            page.snack_bar.open = True
            new_task.focus()
            page.update()
            return
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=300, height=50)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

ft.app(target=main)
