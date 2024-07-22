import npyscreen as ns

class mySubForm(ns.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def beforeEditing(self) -> None:
        pass

    def while_editing(self, e) -> None:
        pass

    def while_waiting(self, e) -> None:
        pass

    def create(self):
        pass

    def afterEditing(self) -> None:
        self.parentApp.setNextForm('MAIN')
        pass


# class myForm(ns.Form):
# class myForm(ns.SplitForm):
class myForm(ns.FormWithMenus):
# class myForm(ns.ActionFormV2WithMenus):

    OK_BUTTON_TEXT = 'Exit'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.__class__.MENU_KEY = '^M'
        # self.MENU_KEY = '^M'
        self.MENU_WIDTH = 40
        self.BLANK_COLUMNS_RIGHT = 2
        self.BLANK_LINES_BASE = 2
        self.cycle_widgets = True
        # shift Form by y
        self.show_aty = 0

    def beforeEditing(self) -> None:
        pass

    def while_editing(self, e) -> None:
        pass

    def while_waiting(self, e) -> None:
        pass

    def create(self):
        # subform1 = mySubForm(lines=10, columns=20, minimum_lines=10, minimum_columns=20)
        # self.add(subform1, name=None)

        

        self.add(ns.BoxTitle, name='box1', footer='myFooter', max_height=10, relx=5)
        self.add(ns.BoxTitle, name='box1', footer='myFooter', max_height=10)

        self.menu = self.new_menu(name='123')
        
        self.menu.addItem(
                text=f'{self.MENU_KEY}',
                onSelect=None,
                shortcut=None,
                arguments=None,
                document='doc',
                keywords=None)
        self.menu.addItem(
                text=f'{self.MENU_WIDTH}',
                onSelect=None,
                shortcut=None,
                arguments=None,
                keywords=None)
        self.menu.addNewSubmenu(
                name='sub123',
                shortcut=None,
                preDisplayFunction=None,
                pdfuncArguments=None,
                pdfuncKeywords=None)
        # self.menu2 = self.new_menu(name='23')
        # self.menu.addSubmenu(self.menu2)
        pass

    def afterEditing(self) -> None:
        self.parentApp.setNextForm(None)
        pass




class myApp(ns.NPSAppManaged):

    def onStart(self) -> None:

        form1 = myForm(lines=25, columns=60, minimum_lines=10, minimum_columns=20)
        self.registerForm('MAIN', form1)

        pass


if __name__ == '__main__':

    app = myApp()
    app.run()
