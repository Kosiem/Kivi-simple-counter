from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout

from kivy.clock import Clock
from kivy.core.window import Window

Window.size = (1000, 500)

class Counter(BoxLayout):

    start = StringProperty("1")
    countStart = 1

    def onstart(self):
        self.Clockbase = Clock
        Clock.schedule_interval(self.count, 0.5)
        self.ids.start.disabled = True

    def count(self, *args):
        self.start = str(self.countStart)
        self.countStart += 1

    def onreset(self):
        self.start = str("1")
        self.countStart = 1;
        self.ids.start.disabled = False
        self.ids.pause.disabled = False

    def onstop(self):
        self.Clockbase.unschedule(self.count)
        self.ids.start.disabled = False
        self.start = "Reset counter"
        self.ids.start.disabled = True
        self.ids.pause.disabled = True



class Counter(App):

    pass

Counter().run()