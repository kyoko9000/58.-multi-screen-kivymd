# ****************kivyMD GUI **********************************
from kivy import Config
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, ImageLeftWidget, ThreeLineAvatarListItem, OneLineAvatarListItem
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.toolbar import MDToolbar

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
Config.write()


class MainWindow(MDScreen):
    def __init__(self):
        super(MainWindow, self).__init__()

        sv = ScrollView()
        ml = MDList()
        sv.add_widget(ml)

        sv_1 = ScrollView()
        ml_1 = MDList()
        sv_1.add_widget(ml_1)

        contacts = [
            "tom", "jerry", "doremon", "nobita",
            "jaen", "heroic", "rius", "hera",
            "kira", "terry"
        ]
        pics = [
            "1.jpg", "2.jpg", "3.jpg", "4.jpg",
            "5.jpg", "6.jpg", "7.jpg", "8.jpg",
            "9.jpg", "10.jpg"
        ]
        for i, j in zip(contacts, pics):
            item = ThreeLineAvatarListItem(
                text=i,
                secondary_text="Secondary text here",
                tertiary_text="fit more text than usual",
                _txt_left_pad="100dp"
            )
            image = ImageLeftWidget()
            image.source = "pics/{}".format(j)
            image.radius = [25, 25, 25, 25]
            item.add_widget(image)

            ml.add_widget(item)
            item.bind(on_press=self.dosomething)

        for i, j in zip(contacts, pics):
            item_1 = OneLineAvatarListItem(
                text=i
            )
            image_1 = ImageLeftWidget()
            image_1.source = "pics/{}".format(j)
            image_1.radius = [25, 25, 25, 25]
            item_1.add_widget(image_1)

            ml_1.add_widget(item_1)

        box = BoxLayout(
            orientation='vertical'
        )
        toolbar = MDToolbar(
            title="Menu",
        )
        # toolbar.md_bg_color = [1, 0.2, 0.2, 1]
        toolbar.left_action_items = [["menu", lambda x: print('menu')]]
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

        item_1.add_widget(sv)
        item_2.add_widget(sv_1)
        item_3.add_widget(label_3)
        bottom.add_widget(item_1)
        bottom.add_widget(item_2)
        bottom.add_widget(item_3)

        box.add_widget(toolbar)
        box.add_widget(bottom)
        self.add_widget(box)

    def dosomething(self, x):
        print("click", x.text)


class MyApp(MDApp):
    def __init__(self):
        super().__init__()

    def build(self):
        return MainWindow()


if __name__ == '__main__':
    MyApp().run()
