from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
#from Components import ControlPanel
from controlpanel import ControlPanel
Window.minimum_width,Window.minimum_height = (700,500)

#============to remove when segregate grapher func==================
from matplotlib import style
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
style.use("dark_background")
#=================================================================
KV = '''

'''
plt.plot([1,23,2,5])
plt.ylabel('some number')

class Tab(FloatLayout,MDTabsBase):
	pass
class Graph(BoxLayout):
	pass

class Grapher(BoxLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.add_widget(FigureCanvasKivyAgg(plt.gcf()))

class LogTable(BoxLayout):
	pass

class GraphProperties(BoxLayout):
	pass

class Logger(BoxLayout):
	pass 

class TestUI(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		return Builder.load_file("UI/mdmain.kv")

TestUI().run()

	