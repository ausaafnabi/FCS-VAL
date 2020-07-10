from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
#:import color kivy.utils.get_color_from_hex
BoxLayout:
	orientation: 'vertical'
	MDToolbar:
		size_hint_y: .1
		title: "FCS-VAL"
		md_bg_color: app.theme_cls.bg_dark
	BoxLayout:
		orientation: 'horizontal'
		size_hint_x: .9
		MDCard:
			orientation: 'vertical'
			size_hint_x: .05
			spacing: 5
			Button:
				text: "1"
				size: (30,30)  
				halign: "center"
			Button:
				text: "2"
				size: (30,30)
				halign: "center"
			Button:
				text: "3"
				size: (30,30)
				halign: "center"
		
		BoxLayout:
			orientation: 'vertical'
			size_hint_x: .65
			padding: [10 , 10]
			spacing: 10
			MDCard:
				size_hint_y: .65
				md_bg_color: app.theme_cls.bg_darkest
				BoxLayout:
					orientation: "vertical"
					MDToolbar:
						title: "Behaviours"
						#size_hint_y: .05
						md_bg_color: color("#FF0066")
					Label:
						text: "ControlPanel"
						#size_hint_y: .95
						halign: "center"
			MDCard:
				size_hint_y: .25
				md_bg_color: app.theme_cls.bg_darkest
				BoxLayout:
					orientation: "vertical"
					MDToolbar:
						title: "Logger"
						#size_hint_y: .05
						md_bg_color: color("#FF0066")
					Label:
						text: "Logger"
						#size_hint_y: .95
						halign: "center"
		BoxLayout:
			orientation: 'vertical'
			padding: [5,5]
			size_hint_x: .2
			MDCard:
				#MDRaisedButton:
				#	text: "ControlPanel"
		
		BoxLayout:
			orientation: 'vertical'
			size_hint_x: .45
			padding: [10,10]	
			spacing: 10
			MDCard:
				MDLabel:
					text: "Graph1"
					halign: "center"
			MDCard:
				MDLabel:
					text: "Log"
					halign: "center"

'''


class TestUI(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		return Builder.load_string(KV)

TestUI().run()

	