# ****************kivyMD GUI **********************************
from kivy import Config
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem, ThreeLineListItem, OneLineAvatarListItem, \
    ImageLeftWidget, TwoLineAvatarListItem, ThreeLineAvatarListItem
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
Config.write()


class MainWindow(MDScreen):
    def __init__(self):
        super(MainWindow, self).__init__()
        sv = ScrollView()
        ml = MDList()
        sv.add_widget(ml)
        self.add_widget(sv)

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
            # *************** no icon *************************
            # item = OneLineListItem(
            #     text=i
            # )
            # item = TwoLineListItem(
            #     text=i,
            #     secondary_text="Secondary text here"
            # )
            item = ThreeLineListItem(
                text=i,
                secondary_text="This is a multi-line label where you can",
                tertiary_text="fit more text than usual"
            )

            # *************** icon *************************
            # item = OneLineAvatarListItem(
            #     text=i
            # )
            # item = TwoLineAvatarListItem(
            #     text=i,
            #     secondary_text="Secondary text here"
            # )
            # item = ThreeLineAvatarListItem(
            #     text=i,
            #     secondary_text="Secondary text here",
            #     tertiary_text="fit more text than usual",
            #     _txt_left_pad="100dp"
            # )
            # image = ImageLeftWidget()
            # image.source = "pics/{}".format(j)
            # image.radius = [25, 25, 25, 25]
            # item.add_widget(image)

            ml.add_widget(item)
            item.bind(on_press=self.dosomething)

    def dosomething(self, x):
        print("click", x.text)


class MyApp(MDApp):
    def __init__(self):
        super().__init__()

    def build(self):
        return MainWindow()


if __name__ == '__main__':
    MyApp().run()