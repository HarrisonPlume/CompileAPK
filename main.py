
from kivymd.app import MDApp
from kivy.lang import Builder
import requests
import time



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
        return Builder.load_file("main.kv")

Main().run()
