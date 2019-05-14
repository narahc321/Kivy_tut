from kivy.app import App
#kivy.require("1.8.0s")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.graphics import Line
# from kivy.uix.floatlayout import FloatLayout


# from kivy.uix.label import Label
from kivy.uix.widget import Widget
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput


# class LoginScreen(GridLayout):
# 	def __init__(self, **kwargs):
# 		super(LoginScreen, self).__init__(**kwargs)
# 		self.cols = 2
		
# 		self.add_widget(Label(text="Username:"))
# 		self.username=TextInput(multiline=False)
# 		self.add_widget(self.username)

# 		self.add_widget(Label(text="password:"))
# 		self.password=TextInput(multiline=False,password=True)
# 		self.add_widget(self.password)
		

# class simplekivy(App):
# 	def build(self):
# 		return Label()


# if __name__ == "__main__":
# 	simplekivy().run()


# class Widgets(Widget):
# 	pass

# class simplekivy2(App):
# 	def build(self):
# 		return Widgets()


# class Widgets(Widget):
# 	pass

# class simplekivy3(App):
# 	def build(self):
# 		return Widgets()


# class TouchInput(Widget):
# 	def on_touch_down(self, touch):
# 		print(touch)

# 	def on_touch_move(self, touch):
# 		print(touch)
# 	def on_touch_up(self, touch):
# 		print("released",touch)

# class simplekivy4(App):
# 	def build(self):
# 		return TouchInput()

# class DrawInput(Widget):
# 	def on_touch_down(self, touch):
# 		print(touch)
# 		with self.canvas:
# 			touch.ud["line"] = Line(points=(touch.x, touch.y))
# 	def on_touch_move(self, touch):
# 		print(touch)
# 		with self.canvas:
# 			touch.ud["line"].points += (touch.x, touch.y)
# 	def on_touch_up(self, touch):
# 		print("released",touch)

# class simplekivy4(App):
# 	def build(self):
# 		return DrawInput()

class MainScreen(Screen):
	pass

class AnotherScreen(Screen):
	pass

class ScreenManagement(ScreenManager):
	pass

class Painter(Widget):
	def on_touch_down(self, touch):
		print(touch)
		with self.canvas:
			touch.ud["line"] = Line(points=(touch.x, touch.y))
	def on_touch_move(self, touch):
		print(touch)
		with self.canvas:
			touch.ud["line"].points += (touch.x, touch.y)
	def on_touch_up(self, touch):
		print("released",touch)

		

presentation = Builder.load_file("main2.kv")
class MainApp(App):
	def build(self):
		return presentation

if __name__ == "__main__":
	MainApp().run()
