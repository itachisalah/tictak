
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('slider.kv')

class MyLayout(Widget):
    def change_value(self,*args):
        self.ids.slider_text.text = str(args[1])
        self.ids.slider_text.font_size=str(args[1])


class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
