from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase


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
			Label:
				text: ""
				size_hint_y: .05
			Button:
				text: "1"
				size_hint_y: .1   
				halign: "center"
			Button:
				text: "2"
				size_hint_y: .1 
				halign: "center"
			Button:
				text: "3"
				size_hint_y: .1
				halign: "center"
			Label:
				text: ""
		
		BoxLayout:
			orientation: 'vertical'
			size_hint_x: .65
			padding: [10 , 10]
			spacing: 10
			MDLabel:
				text: "DashBoard"
				font_style: "H3"
				size_hint_y: .1
			MDCard:
				size_hint_y: .55
				md_bg_color: app.theme_cls.bg_darkest
				radius: [20,10,20,10]
				BoxLayout:
					orientation: "vertical"
					MDToolbar:
						title: "Behaviours"
						size_hint_y: .1
						md_bg_color: color("#FF0066")
					Label:
						text: "ControlPanel"
						size_hint_y: .9
						halign: "center"
			MDCard:
				size_hint_y: .25
				md_bg_color: app.theme_cls.bg_darkest
				radius: [20,10,20,10]
				BoxLayout:
					orientation: "vertical"
					MDToolbar:
						title: "Logger"
						size_hint_y: .2
						md_bg_color: color("#FF0066")
					Label:
						text: "Logger"
						size_hint_y: .8
						halign: "center"
		BoxLayout:
			orientation: 'vertical'
			padding: [5,5]
			size_hint_x: .2
			MDCard:
				radius: [20,10,20,10]
				BoxLayout:
					orientation: 'vertical'
					MDToolbar:
						title: 'graph properties'
						md_bg_color: color("#FF0066")
				#MDRaisedButton:
				#	text: "ControlPanel"
		
		BoxLayout:
			orientation: 'vertical'
			size_hint_x: .45
			padding: [10,10]	
			spacing: 10
			MDCard:
				radius: [20,10,20,10]
				MDLabel:
					text: "Graph1"
					halign: "center"
			MDCard:
				radius: [20,10,20,10]
				MDLabel:
					text: "Log"
					halign: "center"
		#MDFloatingActionButton:
		#	icon: "plus"
		#	pos: 20,20
'''

class Tab(FloatLayout,MDTabsBase):
	pass

class TestUI(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		return Builder.load_string(KV)

TestUI().run()

	