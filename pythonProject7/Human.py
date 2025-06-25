import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import button


class SpartanGrid(GridLayout):
    def __int__(self,**kwargs):
        super(SpartanGrid,self).__init__()
        self.cols =2

        self.add_widget(Label(text= "Student Name" ))

        self.s_name = TextInput(multiline=False)
        self.add_widget(self.s_name)

    def click_me(self,instance):
        print("You have entered your details succescfully")



class SpartanApp(App):
    def build(self):
        return SpartanGrid()

if __name__ == "__main__":
    SpartanApp().run()








