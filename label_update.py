from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField


class Test(MDApp):
    def __init__(self):
        super().__init__()
        self.textedit = None
        self.update_signal = None
        self.count = 0
        self.label = None
        self.list = ["0s", "1s", "2d", "3a", "4y", "5s", "6d", "7a", "8y"]

    def build(self):
        screen = MDScreen()
        layout = MDBoxLayout(orientation="vertical")
        self.label = MDLabel(
            text="0",
            halign="center",
        )
        self.textedit = MDTextField(
            hint_text="Round mode",
            mode="round",
            max_text_length=15,
            helper_text="Massage"
        )
        button = MDRaisedButton(
            text="MDRaisedButton",
            md_bg_color="red",
        )
        button.bind(on_press=self.hello)
        button_1 = MDRaisedButton(
            text="MDRaisedButton_1",
            md_bg_color="red",
        )
        button_1.bind(on_press=self.hello_1)

        screen.add_widget(layout)
        layout.add_widget(self.label)
        layout.add_widget(self.textedit)
        layout.add_widget(button)
        layout.add_widget(button_1)
        return screen

    def hello(self, r):
        self.update_signal = Clock.schedule_interval(self.tt, 1)

    def hello_1(self, r):
        self.update_signal.cancel()

    def tt(self, x):
        self.count += 1
        print(self.count)
        self.label.text = self.list[self.count]
        if self.count == 8:
            self.update_signal.cancel()

        # a = self.textedit.text
        # if a == "e":
        #     self.update_signal.cancel()
        # else:
        #     print(a)
        #     self.label.text = str(a)


Test().run()
