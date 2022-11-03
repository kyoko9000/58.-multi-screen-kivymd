import random
import threading
import time

from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField


class Test(MDApp):
    def __init__(self):
        super().__init__()
        self.stop_thr = None
        self.num_thread = None
        self.textedit = None
        self.data_tables = None
        self.list = ["0s", "1s", "2s", "3s", "4s", "5s", "6s", "7s",
                     "8s", "9s", "10s", "11s", "12s", "13s", "14s", "15s"]

    def build(self):
        screen = MDScreen()
        layout = MDBoxLayout(orientation="vertical")
        layout_table = MDAnchorLayout()
        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.9),
            use_pagination=True,
            check=True,
            column_data=[
                ("State", dp(30)),
                ("Data", dp(20)),
                ("Thread", dp(20))
            ]
        )
        self.textedit = MDTextField(
            hint_text="Round mode",
            mode="round",
            max_text_length=15,
        )
        button = MDRaisedButton(
            text="start",
            md_bg_color="red",
        )
        button.bind(on_press=self.run_threading)
        button_1 = MDRaisedButton(
            text="stop",
            md_bg_color="red",
        )
        button_1.bind(on_press=self.stop_thread)

        layout_table.add_widget(self.data_tables)
        layout.add_widget(layout_table)
        layout.add_widget(self.textedit)
        layout.add_widget(button)
        layout.add_widget(button_1)
        screen.add_widget(layout)
        return screen

    def stop_thread(self, x):
        self.stop_thr = 1

    def run_threading(self, x):
        self.num_thread = int(self.textedit.text)
        self.data_tables.row_data = [
            (
                "_",
                "_",
                "_",
            ) for i in range(self.num_thread)
        ]
        for i in range(self.num_thread):
            t1 = threading.Thread(target=self.active_, args=(i,))
            t1.start()

    def active_(self, i):
        print("thread", i)
        random_number = random.randint(0, 4)

        state = "run"
        count = random_number
        self.stop_thr = 0
        while True:
            self.data_tables.update_row(
                self.data_tables.row_data[i],  # old row data
                [state, self.list[count], "Thread: {}".format(i)],  # new row data
            )
            time.sleep(1)
            count += 1
            if count == 15:
                state = "stop"
                self.data_tables.update_row(
                    self.data_tables.row_data[i],  # old row data
                    [state, self.list[count], "Thread: {}".format(i)],  # new row data
                )
                break
            elif self.stop_thr == 1:
                state = "stop"
                self.data_tables.update_row(
                    self.data_tables.row_data[i],  # old row data
                    [state, self.list[count], "Thread: {}".format(i)],  # new row data
                )
                print("stop thread")
                break


Test().run()
