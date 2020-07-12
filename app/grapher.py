import random
from matplotlib import style
from matplotlib import pyplot as plt
from kivy.app import App
from matplotlib import use as mpl_use

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
form kivy.clock import Clock
import kivy.properties as kp

mpl_use('model://kivy.garden.matplotlib.backend_kivyagg')
style.use("dark_background")

class TestApp(App):
	def build(self):
		return Builder.load_string("Chart:")

class Chart(BoxLayout):
	data= kp.ListProperty([])
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.fig, self.ax1 = plt.subplots()
		self.ax1.plot([],[],'bo')
		self.mpl_canvas = self.fig.canvas
		self.add_widget(self.mpl_canvas)
		Clock.schedule_interval(self.update,1)
	def on_data(self,*args):
		self.ax1.clear()
		y = [i**2 for i in self.data]
		self.ax1.plot(self.data,y,'bo-',linewidth=5.0)
		self.mpl_canvas.draw_idle()
	def update(self,*args):
		self.data = random.sample(range(-10,10),5)

if __name__ == "__main__":
	TestApp().run()