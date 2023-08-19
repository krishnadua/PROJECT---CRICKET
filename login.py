import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Krishna(App):
	def build(self):
		B = BoxLayout(orientation="vertical")
		T = TextInput(text="" , halign="center")
		Ti = TextInput(text="" , halign="center")
		Bu = Button(text="Sign Up" , halign="center" , background_color=(1,1,6,1))
		
		B.add_widget(T)
		B.add_widget(Ti)
		B.add_widget(Bu)
		
		return B
		
Krishna().run()