# ****************kivyMD GUI **********************************
from kivy import Config
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.textinput import TextInput
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
Config.write()


class MainWindow(MDScreen):
    def __init__(self):
        super(MainWindow, self).__init__()
        BoxLayout2 = MDFloatLayout(
            size_hint=(None, None),
            size=(350, 250),
            pos_hint={"center_x": 0.5, "center_y": 0.75}
        )
        with BoxLayout2.canvas:
            Color(1, 0.8, 0.8, 1)
            BoxLayout2.rect = RoundedRectangle(
                pos=BoxLayout2.pos,
                size=BoxLayout2.size,
                radius=[(15, 15), (15, 15), (15, 15), (15, 15)],
            )
        BoxLayout2.bind(pos=lambda obj, pos: setattr(BoxLayout2.rect, "pos", pos))
        BoxLayout2.bind(size=lambda obj, size: setattr(BoxLayout2.rect, "size", size))

        # BoxLayout2.size_hint = (None, None)
        # BoxLayout2.size = (350, 250)
        # BoxLayout2.pos_hint = {"center_x": 0.5, "center_y": 0.75}

        text = TextInput(
            hint_text="Title",
            size_hint=[1, None],  # space to put text
            pos_hint={"center_x": .5, "center_y": 0.5},
            height=BoxLayout2.height,
            multiline=True,
            cursor_color=[255 / 255, 170 / 255, 23 / 255, 1],
            cursor_width="2sp",
            foreground_color=[1, 170 / 255, 23 / 255, 1],  # text color
            background_color=[0, 0, 0, 0],  # invisible background
            padding=15,  # distance from border
            font_size="30sp"  # text size
        )

        BoxLayout2.add_widget(text)
        self.add_widget(BoxLayout2)


class MyApp(MDApp):
    def __init__(self):
        super().__init__()

    def build(self):
        return MainWindow()


if __name__ == '__main__':
    MyApp().run()