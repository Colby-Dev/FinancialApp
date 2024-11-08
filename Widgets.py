import kivy
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout




# class LblApp(App):
#     def build(self):
#         lbl = Label(text='test')
#         return lbl
#
#
# if __name__ == '__main__':
#     label = LblApp()
#     label.run()

# class Canvas(Widget):
#
#     def __init__(self, **kwargs):
#         super(Canvas, self).__init__(**kwargs)
#
#         with self.canvas:
#             Color(1,1,1,1)
#
#             self.rect = Rectangle(
#                                   pos=self.pos,
#                                   size=self.size)
#
#             self.bind(pos=self.update_rect,
#                       size=self.update_rect)
#
#     def update_rect(self, *args):
#         self.rect.pos = self.pos
#         self.rect.size = self.size

class CanvasApp(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.testText = Label(text="Testing")
        self.testInput = TextInput(text="")

        # # b = BoxLayout(orientation='vertical')
        # # t = TextInput(font_size = 50,
        # #               size_hint_y = None,
        # #               height = 100)
        # label = Label(text='Testing',
        #               font_size=50,
        #               pos_hint={'bottom': 1.5, 'center_x': 0.3})
        # stocksTextBox = TextInput(text='',
        #                           height = 50,
        #                           size_hint = (.5, .25),
        #                           pos = (20,20))
        # float = FloatLayout(size=(100,200))
        # float.add_widget(label)
        # float.add_widget(stocksTextBox)
        # self.window.add_widget(float)
        self.window.add_widget(self.testText)
        self.window.add_widget(self.testInput)
        return self.window