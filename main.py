import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy import Config
Config.set('graphics', 'multisamples', '0')

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

Builder.load_file('design.kv')


class LoginScreen(Screen):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
