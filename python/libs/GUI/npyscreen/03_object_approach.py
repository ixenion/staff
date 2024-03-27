import npyscreen

class myEmployeeForm(npyscreen.Form):

    # def __init__(self, *args, **kwargs):
    #     super().__init__()
        # self.lines = 3
        # self.columns = 22
        # self.minimum_lines = 2
        # self.minimum_columns = 20

    def afterEditing(self):
        self.parentApp.setNextForm(None)
        # self.parentApp.setNextForm('MAIN2')
        # self.parentApp.switchForm('MAIN2')

    def create(self):
       self.myName        = self.add(npyscreen.TitleText, name='Name')
       self.myDepartment = self.add(
               npyscreen.TitleSelectOne,
               scroll_exit=True,
               max_height=3,
               name='Department',
               values = ['Department 1', 'Department 2', 'Department 3']
               )
       self.nextrely += 5
       self.myDate = self.add(npyscreen.TitleDateCombo, name='Date Employed')


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
