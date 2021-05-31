import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Inicia keywords infinitas
    def __init__(self, **kwargs):
        # Chama contrutor de layout de grades
        super(MyGridLayout, self).__init__(**kwargs)  # Configurando as colunas
        self.cols = 2

        self.add_widget(Label(text='Nome: '))  # Adicionando widgets
        self.nome = TextInput(multiline=False)  # Adicionando caixa input
        self.add_widget(self.nome)

        self.add_widget(Label(text='Sobrenome: '))  # Adicionando widgets
        self.sobrenome = TextInput(multiline=False)  # Adicionando caixa input
        self.add_widget(self.sobrenome)

        self.submit = Button(text='Mandar', font_size=18)  # Criando o botão submit
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        nome = self.nome.text
        sobrenome = self.sobrenome.text

        self.add_widget(Label(text=f'Olá {sobrenome} {nome}...'))

        self.nome.text = ''
        self.sobrenome.text = ''

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()

