from kivy.uix.boxlayout import BoxLayout
from matplotlib import style
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
style.use("dark_background")

plt.plot([1,23,2,5])
plt.ylabel('some number')

class Grapher(BoxLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.add_widget(FigureCanvasKivyAgg(plt.gcf()))
