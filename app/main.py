import kivy
from kivymd.app import MDApp as App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
#from kivymd.uix.scree
kivy.require('1.9.0')

Window.size=(800,600)
Window.minimum_width,Window.minimum_height = (400,300)

Builder.load_file("UI/Components/Header.kv")
Builder.load_file("UI/Components/GraphPanel.kv")
Builder.load_file("UI/Components/Sidebar.kv")
k = Builder.load_file("UI/main.kv")

class Header():
	pass
class GraphPanel():
	pass
class Sidebar():
	pass

class main(Screen):
	def build(self):
		pass	
	def open_graph(self):
        	from subprocess import Popen,PIPE
        	process = Popen(['python3', '../tools/FCConn.py'],stdout=PIPE,stderr=PIPE)

screen_manager = ScreenManager()
#screen_manager.add_widget(launcher(name="launcher"))
screen_manager.add_widget(main(name="main"))


class mainApp(App):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("UI/main.kv")

if __name__ == "__main__":
	mainApp().run()