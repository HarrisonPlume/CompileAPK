
from kivymd.app import MDApp
from kivy.lang import Builder
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

    
    def actionoff(self):
        label = self.root.ids.txt
        label.text = "LED OFF"

    def build(self):
        return Builder.load_file("main.kv")

Main().run()
