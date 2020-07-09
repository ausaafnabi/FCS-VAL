import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
kivy.require('1.9.0')

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.config import Config

#Config.set('graphics','fullscreen','auto')
Window.size=(Window.width,400)
Window.borderless=True

Builder.load_file("UI/launcher.kv")

class launcher(Screen):
    def build(self):
        pass    
    def open_launcher_with_device(self):
        from subprocess import Popen,PIPE
        process = Popen(['python3','main.py'],stdout=PIPE,stderr=PIPE)

screen_manager = ScreenManager()

screen_manager.add_widget(launcher(name="launcher"))
#screen_manager.add_widget(main(name="main"))

class launcherApp(App):
    def build(self):
        #button = Button(text="Exit",size_hint=(0.2,0.1))
        return launcher()

launcher_app = launcherApp()
launcher_app.run()

