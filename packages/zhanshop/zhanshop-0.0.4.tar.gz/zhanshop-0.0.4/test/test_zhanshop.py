import os
from zhanshop import App

App(os.path.dirname(os.path.abspath(__file__)))

print(App.rootPath)