# ****************kivyMD GUI **********************************
from kivy import Config
from kivy.graphics import Color, Rectangle
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationLayout, MDNavigationDrawerMenu, \
    MDNavigationDrawerHeader, MDNavigationDrawerLabel, MDNavigationDrawerDivider, MDNavigationDrawerItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.toolbar import MDTopAppBar

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
Config.write()


class MainWindow(MDScreen):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.box_navi = MDNavigationLayout()
        toolbar = MDTopAppBar(
            title="Menu",
        )
        toolbar.left_action_items = [["menu", lambda x: self.show_example_grid_bottom_sheet(x)]]
        toolbar.right_action_items = [["logout", lambda x: print('exit')]]

        bottom = MDBottomNavigation()
        with bottom.canvas:
            Color(33 / 255, 150 / 255, 243 / 255, 0.3)
            bottom.rect = Rectangle(
                pos=bottom.pos,
                size=bottom.size,
            )
        bottom.bind(pos=lambda obj, pos: setattr(bottom.rect, "pos", pos))
        bottom.bind(size=lambda obj, size: setattr(bottom.rect, "size", (bottom.width, 56.0)))

        item_1 = MDBottomNavigationItem(
            name='screen 1',
            text='main',
            icon='home'
        )
        label_1 = MDLabel(
            text='main screen',
            halign='center'
        )
        item_2 = MDBottomNavigationItem(
            name='screen 2',
            text='contacts',
            icon='contacts'
        )
        label_2 = MDLabel(
            text='sub screen 1',
            halign='center'
        )
        item_3 = MDBottomNavigationItem(
            name='screen 3',
            text='account',
            icon='account'
        )
        label_3 = MDLabel(
            text='sub screen 2',
            halign='center'
        )

        item_1.add_widget(label_1)
        item_2.add_widget(label_2)
        item_3.add_widget(label_3)

        bottom.add_widget(item_1)
        bottom.add_widget(item_2)
        bottom.add_widget(item_3)

        screen_2 = MDBoxLayout(orientation='vertical')
        screen_2.add_widget(toolbar)
        screen_2.add_widget(bottom)
        screen_1 = MDScreen(screen_2)
        screen_m = MDScreenManager(screen_1)

        self.box_navi.add_widget(screen_m)
        self.add_widget(self.box_navi)

    def callback_for_menu_items(self, *args):
        print(args[0])

    def show_example_grid_bottom_sheet(self, x):
        navi_drawer = MDNavigationDrawer(
            radius=(0, 16, 16, 0)
        )
        self.box_navi.add_widget(navi_drawer)
        navi_drawer.add_widget(
            MDNavigationDrawerMenu(
                MDNavigationDrawerHeader(
                    title="Header title",
                    title_color="#4a4939",
                    text="Header text",
                    spacing="4dp",
                    padding=("12dp", 0, 0, "56dp"),
                ),
                MDNavigationDrawerLabel(
                    text="Mail",
                ),
                MDNavigationDrawerItem(
                    radius=24,
                    text_color="#4a4939",
                    icon_color="#4a4939",
                    focus_color="#e7e4c0",
                    icon="yahoo",
                    text="yahoo",
                ),
                MDNavigationDrawerItem(
                    radius=24,
                    text_color="#4a4939",
                    icon_color="#4a4939",
                    focus_color="#e7e4c0",
                    icon="gmail",
                    text="gmail",
                )
                ,
                MDNavigationDrawerDivider(),
                MDNavigationDrawerLabel(
                    text="movies",
                ),
                MDNavigationDrawerItem(
                    radius=24,
                    text_color="#4a4939",
                    icon_color="#4a4939",
                    focus_color="#e7e4c0",
                    icon="youtube",
                    text="youtube",
                ),
                MDNavigationDrawerItem(
                    radius=24,
                    text_color="#4a4939",
                    icon_color="#4a4939",
                    focus_color="#e7e4c0",
                    icon="facebook",
                    text="facebook",
                )
            ),
        )
        navi_drawer.set_state("open")


class MyApp(MDApp):
    def __init__(self):
        super().__init__()

    def build(self):
        return MainWindow()


if __name__ == '__main__':
    MyApp().run()
