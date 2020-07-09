import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
kivy.require('1.9.0')

Window.size=(800,600)
Window.minimum_width,Window.minimum_height = (400,300)

Builder.load_file("UI/Components/Header.kv")
Builder.load_file("UI/Components/GraphPanel.kv")
Builder.load_file("UI/Components/Sidebar.kv")
Builder.load_file("UI/main.kv")

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
        #button = Button(text="Exit",size_hint=(0.2,0.1))
        return main()

if __name__ == "__main__":
	mainApp().run()