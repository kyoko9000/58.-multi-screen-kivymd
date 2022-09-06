# ****************kivyMD GUI **********************************
from kivy import Config
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer, MDNavigationDrawerMenu, \
    MDNavigationDrawerHeader, MDNavigationDrawerLabel, MDNavigationDrawerDivider, MDNavigationDrawerItem
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.toolbar import MDTopAppBar

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
Config.write()


class MainWindow(MDScreen):
    def __init__(self):
        super(MainWindow, self).__init__()
        box = BoxLayout(
            orientation='vertical'
        )
        toolbar = MDTopAppBar(
            title="Menu",
        )
        # toolbar.md_bg_color = [1, 0.2, 0.2, 1]
        toolbar.left_action_items = [["menu", lambda x: self.show_left_menu_sheet(x)]]
        toolbar.right_action_items = [["logout", lambda x: print('exit')]]

        bottom = MDBottomNavigation()
        # bottom.md_bg_color = [0.4, 0.4, 0.4, 1]
        # bottom.panel_color = [0.2, 0.2, 0.2, 1]
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
        # menu
        self.navi_drawer = MDNavigationDrawer(
            MDNavigationDrawerMenu(
                MDNavigationDrawerHeader(
                    title="Header title",
                    text="Header text",
                    spacing="4dp",
                    padding=["12dp", 0, 0, "56dp"]
                ),
                MDNavigationDrawerLabel(
                    text="Mail",
                ),
                MDNavigationDrawerItem(
                    radius=24,
                    text_color="#4a4939",
                    icon_color="#4a4939",
                    # focus_color="#e7e4c0",
                    icon="yahoo",
                    text="yahoo",
                    right_text="+995",
                    on_press=self.callback_for_menu_items
                ),
                MDNavigationDrawerItem(
                    radius=24,
                    text_color="#4a4939",
                    icon_color="#4a4939",
                    focus_color="#e7e4c0",
                    icon="gmail",
                    text="gmail",
                    on_press=self.callback_for_menu_items
                ),
                MDNavigationDrawerDivider(),
                MDNavigationDrawerLabel(
                    text="movies",
                ),
                MDNavigationDrawerItem(
                    radius=24,
                    text_color="#4a4939",
                    icon_color="#4a4939",
                    focus_color="#e7e4c0",
                    ripple_color="#c5bdd2",
                    selected_color="#0c6c4d",
                    icon="youtube",
                    text="youtube",
                    on_press=self.callback_for_menu_items
                ),
                MDNavigationDrawerItem(
                    radius=24,
                    text_color=[0, 0, 0, 1],
                    icon_color=[0, 0, 0, 1],
                    # focus_color=[1, 0, 0, 1],
                    ripple_color=[0, 0, 0, 1],
                    selected_color=[0, 0, 1, 1],
                    icon="facebook",
                    text="facebook",
                    on_press=self.callback_for_menu_items
                )
            ),
            radius=(16, 0, 0, 16),
            anchor="right"
        )

        item_1.add_widget(label_1)
        item_2.add_widget(label_2)
        item_3.add_widget(label_3)
        bottom.add_widget(item_1)
        bottom.add_widget(item_2)
        bottom.add_widget(item_3)

        box.add_widget(toolbar)
        box.add_widget(bottom)
        screen_1 = MDScreen(box)
        screen_m = MDScreenManager(screen_1)

        self.box_navi = MDNavigationLayout()
        self.box_navi.add_widget(screen_m)
        self.box_navi.add_widget(self.navi_drawer)
        self.add_widget(self.box_navi)

    def callback_for_menu_items(self, *args):
        print("hello")
        self.navi_drawer.set_state("close")

    def show_left_menu_sheet(self, x):
        self.navi_drawer.set_state("open")


class MyApp(MDApp):
    def __init__(self):
        super().__init__()

    def build(self):
        return MainWindow()


if __name__ == '__main__':
    MyApp().run()