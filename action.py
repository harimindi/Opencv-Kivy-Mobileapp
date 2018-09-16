import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import numpy as nu
import cv2


class Controller(BoxLayout):
	def __init__(self):
		super(Controller,self).__init__()

	def btn_clk(self):
		cap = cv2.VideoCapture(0)

		while True:
			ret,frame = cap.read()
			gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
			cv2.imshow('gray',gray) #imgshow
			if cv2.waitKey(20) & 0xFF == ord('q'):
				break
		cap.release

class ActionApp(App):
	def build(self):
		return Controller()

ActionApp().run()