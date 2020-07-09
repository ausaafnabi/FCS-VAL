from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.factory import Factory
from kivy.lang import Builder

Builder.load_string("""
<LabelC>:
	bcolor: 1,1,1,1
	canvas.before:
		Color:
			rgba: self.color
		Rectangle:
			pos: self.pos
			size: self.size
""")

class LabelC(Label):
	bcolor = ListProperty([1,1,1,1])

Factory.register('kivyB',module='LabelC')
#================================================

