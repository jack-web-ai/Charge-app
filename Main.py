from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
class ChargeCalculator(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        self.hours = TextInput(hint_text="Hours to full charge", input_filter="int")
        self.minutes = TextInput(hint_text="Minutes", input_filter="int")
        self.result = Label(text="Result will appear here")
        btn = Button(text="Calculate 80% Time")
        btn.bind(on_press=self.calculate)
        layout.add_widget(self.hours)
        layout.add_widget(self.minutes)
        layout.add_widget(btn)
        layout.add_widget(self.result)
        return layout
    def calculate(self, instance):
        h = int(self.hours.text or 0)
        m = int(self.minutes.text or 0)
        total = h * 60 + m
        t80 = total * 0.8
        hh = int(t80 // 60)
        mm = int(t80 % 60)
        self.result.text = f"80% = {hh} hr {mm} min"
ChargeCalculator().run()
