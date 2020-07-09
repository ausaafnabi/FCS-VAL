from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
#:import color kivy.utils.get_color_from_hex
BoxLayout:
	orientation: 'vertical'
	MDToolbar:
		size_hint_y: .1
		title: "MDToolbar"
		md_bg_color: color("#FF0066")#app.theme_cls.purple_color
	BoxLayout:
		orientation: 'horizontal'
		size_hint_x: .9
		BoxLayout:
			orientation: 'vertical'
			size_hint_x: .05
			MDRectangleFlatButton:
				text: "Hello World"
				halign: "center"
			MDRectangleFlatButton:
				text: "Hello World"
				halign: "center"
			MDRaisedButton:
				text: "Hello World"
				halign: "center"
		
		BoxLayout:
			orientation: 'vertical'
			size_hint_x: .45
			MDLabel:
				text: "ControlPanel"
				halign: "center"
			Label:
				text: "Logger"
				halign: "center"
		
		BoxLayout:
			orientation: 'vertical'

			size_hint_x: .1
			MDRaisedButton:
				text: "ControlPanel"
		
		BoxLayout:
			orientation: 'vertical'
			size_hint_x: .35
			MDLabel:
				text: "ControlPanel"
				halign: "center"
			MDLabel:
				text: "Logger"
				halign: "center"

'''


class TestUI(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		return Builder.load_string(KV)

TestUI().run()

	