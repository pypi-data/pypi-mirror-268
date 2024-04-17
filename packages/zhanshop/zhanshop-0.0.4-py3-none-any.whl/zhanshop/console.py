import importlib

from zhanshop.helper import Helper
from zhanshop.log import Log

class Console():
    """
    指令配置
    """
    commands = {
        'helper': 'zhanshop.command',
        'server': 'zhanshop.command',
    }

    route = None

    def regRoute(self, route):
        self.route = route

    def run(self, app, args):
        if("gunicorn" in args[0]):
            key = 'server'
        else:
            key = Helper.arrKey(args, 1, 'helper')
        # 和用户自定义指令进行合并

        if key not in self.commands:
            return Log.echo("指令"+key+"未注册", "error")

        command = self.commands[key]
        module = importlib.import_module(command)
        className = getattr(module, key)

        myclass = className() # 实例化指令类
        myclass.execute(app, self.route) # 运行指令

    def end(self):
        print("")