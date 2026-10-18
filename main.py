from kivy.app import App
from kivy.uix.label import Label

class HalloApp(App):
    def build(self):
        return Label(text="hallo")

HalloApp().run()
