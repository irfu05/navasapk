from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):

    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text="Name: "))

        self.name = TextInput(multiline=True)
        self.add_widget(self.name)

        self.add_widget(Label(text="Favorite Pizza: "))

        self.pizza = TextInput(multiline=True)
        self.add_widget(self.pizza)

        self.submit = Button(text="Submit", font_size=32)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text

        self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza'))

        self.name.text = ''
        self.pizza.text = ''

class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
