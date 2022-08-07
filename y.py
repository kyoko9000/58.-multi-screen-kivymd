from kivymd.app import MDApp
from kivy.lang import Builder


class Test(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_string(
            '''
BoxLayout:
    orientation:'vertical'

    MDToolbar:
        title: "Demo"
        left_action_items:[["menu",lambda x: app.navigation_draw()]]
        right_action_items:[["logout",lambda x: app.navigation_draw()]]

    MDBottomNavigation:
        panel_color: .2, .2, .2, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'main'
            icon: 'home'

            MDLabel:
                text: 'main screen'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'contacts'
            icon: 'contacts'

            MDLabel:
                text: 'sub screen 1'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'account'
            icon: 'account'

            MDLabel:
                text: 'sub screen 2'
                halign: 'center'
'''
        )


Test().run()