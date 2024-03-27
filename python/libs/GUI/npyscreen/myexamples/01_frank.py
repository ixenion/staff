import npyscreen
from time import sleep

class myEmployeeForm(npyscreen.Form):

    def afterEditing(self):
        self.parentApp.setNextForm(None)
        # self.parentApp.setNextForm('MAIN2')
        # self.parentApp.switchForm('MAIN2')

    def create(self):

       class mySlider(npyscreen.TitleSlider):
           def __init__(self, *args, target_widget, **kwargs):
               super().__init__(*args, **kwargs)
               self.tw = target_widget
               pass
           def when_value_edited(self) -> None:
               self.tw.value = str(self.value)
               self.tw.display()

       self.tw  = self.add(npyscreen.TitleText, name = "Text:",)
       self.fn = self.add(npyscreen.TitleFilename, name = "Filename:")
       self.fn2 = self.add(npyscreen.TitleFilenameCombo, name="Filename2:")
       self.dt = self.add(npyscreen.TitleDateCombo, name = "Date:")
       
       # self.s  = self.add(npyscreen.TitleSlider, out_of=12, name = "Slider")
       self.s  = self.add(mySlider, out_of=12, name = "Slider", target_widget=self.tw)

       self.ml = self.add(npyscreen.MultiLineEdit,
              value = """try typing here!\nMutiline text, press ^R to reformat.\n""",
              max_height=5, rely=9)
       self.ms = self.add(npyscreen.TitleSelectOne, max_height=4, value = [1,], name="Pick One",
               values = ["Option1","Option2","Option3"], scroll_exit=True)
       self.ms2= self.add(npyscreen.TitleMultiSelect, max_height =-2, value = [1,], name="Pick Several",
               values = ["Option1","Option2","Option3"], scroll_exit=True)

    def while_editing(self, e) -> None:
        pass

    def while_waiting(self, e) -> None:
        pass




    def add_divider(self, rows: int) -> None:
        self.nextrely += rows
        # self.nextrelx += rows


class MyApplication(npyscreen.NPSAppManaged):

   def onStart(self):
       # self.addForm(
       #         'MAIN', myEmployeeForm, name='New Employee',
       #         lines=25, columns=60, minimum_lines=10, minimum_columns=20
       #         )

       obj = myEmployeeForm(lines=25, columns=60, minimum_lines=10, minimum_columns=20)
       # obj = myEmployeeForm()
       self.registerForm('MAIN', obj)

       # A real application might define more forms here.......

if __name__ == '__main__':
   TestApp = MyApplication().run()
