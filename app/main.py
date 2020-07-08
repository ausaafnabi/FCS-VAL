import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
kivy.require('1.9.0')

Window.size=(800,600)

kv = Builder.load_file("UI/main.kv")

class mainApp(App):
	def build(self):
		return kv

if __name__ == "__main__":
	mainApp().run()