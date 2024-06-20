
from kivymd.app import MDApp
from kivy.lang import Builder
import requests
import time

kv = """
Screen:
    MDLabel:
        text: ""
        id: txt
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
    MDRaisedButton:
        text: 'LED ON'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press:
            app.actionon()
    MDRaisedButton:
        text: 'LED OFF'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_press:
            app.actionoff()
    MDFillRoundFlatIconButton:
        text: 'MDFillRoundFlatIconButton'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        width: dp(230)
        icon: 'google'
    MDFloatingActionButtonSpeedDial:
        data: app.data
        rotation_root_button: True
"""


class Main(MDApp):
    data = {
        'language-pythonxdr': 'PythonXDR',
        'language-php': 'PHP',
        'language-cpp': 'C++',
    }

    def actionon(self):
        label = self.root.ids.txt
        label.text = "LED ON"
        urlon = "http://192.168.0.196/H"
        for i in range(3):
            print(i)
            try:
                requests.get(urlon, verify=False, timeout=1)
            except:
                pass
            time.sleep(0.01)

    
    def actionoff(self):
        label = self.root.ids.txt
        label.text = "LED OFF"
        urloff = "http://192.168.0.196/L"
        for i in range(3):
            print(i)
            try:
                requests.get(urloff, verify=False, timeout=1)
            except:
                pass
            time.sleep(0.01)

    def build(self):
        return Builder.load_string(kv)


Main().run()