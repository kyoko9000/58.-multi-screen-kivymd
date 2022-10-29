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
        self.count = 0
        self.update_signal = None
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
        )
        button = MDRaisedButton(
            text="MDRaisedButton",
            md_bg_color="red",
        )
        button.bind(on_press=self.active_)
        screen.add_widget(layout)
        layout.add_widget(self.label)
        layout.add_widget(self.textedit)
        layout.add_widget(button)
        return screen

    def active_(self, x):
        self.update_signal = Clock.schedule_interval(self.update, 1)

    def update(self, x):
        # self.label.text = self.list[self.count]
        # self.count += 1
        # if self.count == 9:
        #     self.update_signal.cancel()

        text = self.textedit.text
        print(text)
        self.label.text = str(text)


Test().run()
