import npyscreen as ns

class TestApp(ns.NPSApp):
    def main(self):
        MyForm = ns.Form()
        
        usrn_box = MyForm.add_widget(ns.TitleText, name="Your name:")
        # internet = MyForm.add_widget(ns.TitleText, name="Your favourite internet page:")
        internet = MyForm.add_widget(ns.TitleText, name="Your:")
        
        MyForm.edit()

if __name__ == "__main__":
    App = TestApp()
    App.run()

# usrn_box.value and internet.value now hold the user's answers.
