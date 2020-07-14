#=====================Core Libraries======================
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
#=======================================================

#====================== Modules=========================
#from Components import ControlPanel
from controlpanel import ControlPanel
from graph import Grapher
#=======================================================

#===================Config Properties=====================
Window.minimum_width,Window.minimum_height = (700,500)

#======================Builder Classes====================
Builder.load_file("UI/Components/controlpanel.kv")
Builder.load_file("UI/Components/logger.kv")
Builder.load_file("UI/Components/graphproperties.kv")


#=====================Main Class=========================
class Tab(FloatLayout,MDTabsBase):
	pass

class Graph(BoxLayout):
	pass

class Sidebar(BoxLayout):
	pass


class LogTable(BoxLayout):
	pass

class GraphProperties(BoxLayout):
	pass

class Logger(BoxLayout):
	pass 

class Main(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		return Builder.load_file("UI/mdmain.kv")

Main().run()

	