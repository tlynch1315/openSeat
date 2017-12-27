#!/usr/bin/python

import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class CustomWidget(Widget):
	pass

class CustomWidgetApp(App):
	
	def build(self):
		return TestWidget()

customWidget = CustomWidgetApp()
customWidget.run()
