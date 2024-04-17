from .container import Container
class App(Container):
    # 项目根路径
    rootPath = "还没有初始化"
    def __init__(self, path):
        App.rootPath = path