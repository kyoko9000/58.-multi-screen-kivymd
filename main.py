# ****************kivyMD GUI **********************************
from kivy import Config
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDIconButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
Config.write()


class MainWindow(MDScreen):
    def __init__(self):
        super(MainWindow, self).__init__()
        # ========= Create the screen manager ==============
        self.sm = ScreenManager()

        # screen 1 ****************************************
        Screen_1 = MDScreen()
        Screen_1.name = "screen1"
        floatLayout = MDFloatLayout()
        label = MDLabel(
            text="screen 1",
            pos_hint={"center_x": .7, "center_y": .8},
            font_style="H2"
        )
        # label.font_size = 80
        button_screen_1 = MDIconButton(
            icon="card-plus-outline",
            pos_hint={"center_x": .5, "center_y": .5},
            user_font_size="80sp",
            md_bg_color=[0, 170 / 255, 23 / 255, 1],
            theme_text_color="Custom",
            text_color=[1, 1, 1, 1]
        )
        button_screen_1.bind(on_press=self.screen_2)

        button_screen_2 = MDIconButton(
            icon="card-plus-outline",
            pos_hint={"center_x": .5, "center_y": .3},
            user_font_size="80sp",
            md_bg_color=[0, 170 / 255, 23 / 255, 1],
            theme_text_color="Custom",
            text_color=[1, 1, 1, 1]
        )
        button_screen_2.bind(on_press=self.screen_3)

        floatLayout.add_widget(label)
        floatLayout.add_widget(button_screen_1)
        floatLayout.add_widget(button_screen_2)
        Screen_1.add_widget(floatLayout)

        # screen 2 **********************************************
        Screen_2 = MDScreen()
        Screen_2.name = "screen2"

        BoxLayout2 = MDFloatLayout()
        iconbutton2 = MDIconButton(
            icon="chevron-left",
            user_font_size="60sp",
            pos_hint={"center_y": .95},
            theme_text_color="Custom",
            text_color=[1, 170 / 255, 23 / 255, 1]
        )
        iconbutton2.bind(on_press=self.screen_1)

        label_2 = MDLabel(
            text="screen 2",
            pos_hint={"center_x": .7, "center_y": .5},
            font_style="H2"
        )
        BoxLayout2.add_widget(iconbutton2)
        BoxLayout2.add_widget(label_2)

        Screen_2.add_widget(BoxLayout2)

        # screen 3 ************************************************
        Screen_3 = MDScreen()
        Screen_3.name = "screen3"

        BoxLayout3 = MDFloatLayout()
        iconbutton3 = MDIconButton(
            icon="chevron-left",
            user_font_size="60sp",
            pos_hint={"center_y": .95},
            theme_text_color="Custom",
            text_color=[1, 170 / 255, 23 / 255, 1]
        )
        iconbutton3.bind(on_press=self.screen_1)

        label_3 = MDLabel(
            text="screen 3",
            pos_hint={"center_x": .7, "center_y": .5},
            font_style="H2"
        )
        BoxLayout3.add_widget(iconbutton3)
        BoxLayout3.add_widget(label_3)

        Screen_3.add_widget(BoxLayout3)

        self.sm.add_widget(Screen_1)
        self.sm.add_widget(Screen_2)
        self.sm.add_widget(Screen_3)
        self.sm.current = "screen1"
        self.add_widget(self.sm)

    def screen_1(self, x):
        self.sm.current = "screen1"

    def screen_2(self, y):
        self.sm.current = "screen2"

    def screen_3(self, y):
        self.sm.current = "screen3"


class MyApp(MDApp):
    def __init__(self):
        super().__init__()

    def build(self):
        return MainWindow()


if __name__ == '__main__':
    MyApp().run()