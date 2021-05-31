import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='おはよう御座います', font_size=72, font_name='Arial')

if __name__ == '__main__':
    MyApp().run()

