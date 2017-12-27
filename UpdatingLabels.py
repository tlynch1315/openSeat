#!/usr/bin/python

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from yahoo_finance import Share

import random

#class LabelWidget(BoxLayout):
def change_label_colour(self):
	color = [random.random() for i in xrange(3)] + [1]
	Company = Label(text="Twitter: ")
	Company.color = color
	Company.font_size = 70
#		Company.center_x = 200
#		Company.top = 150


class UpdatingLabelsApp(App):
	def build(self):
#		color = [random.random() for i in xrange(3)] + [1]
#		Company = Label(text='Twitter: ')
#		Company.color = color
		return change_label_colour(self)

if __name__ == "__main__":
	UpdatingLabelsApp().run()
