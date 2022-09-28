# ****************kivyMD GUI **********************************
from kivy import Config
from kivymd.icon_definitions import md_icons
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabs, MDTabsBase
from kivymd.uix.toolbar import MDTopAppBar

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
Config.write()


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class MainWindow(MDScreen):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.icons = list(md_icons.keys())[15:30]
        self.j = 0
        box = MDBoxLayout(
            MDTopAppBar(title="Example Tabs"),
            orientation="vertical",
        )
        tab_ = MDTabs()
        tab_.bind(on_tab_switch=self.on_tab_switchs)
        for tab_name in self.icons:
            self.j += 1
            tab_.add_widget(
                Tab(
                    MDRectangleFlatIconButton(
                        icon=tab_name,
                        icon_size="48sp",
                        pos_hint={"center_x": .5, "center_y": .5},
                        text="M"
                    ),
                    icon=tab_name,
                    title="M" + str(self.j)
                )
            )
        box.add_widget(tab_)
        self.add_widget(box)

    def on_tab_switchs(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        """
        Called when switching tabs.
        type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        param instance_tab: <__main__.Tab object>;
        param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        param tab_text: text or name icon of tab;
        """

        count_icon = instance_tab.icon  # get the tab icon
        print(f"Welcome to {count_icon}' tab'")


class MyApp(MDApp):
    def __init__(self):
        super().__init__()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return MainWindow()


if __name__ == '__main__':
    MyApp().run()
