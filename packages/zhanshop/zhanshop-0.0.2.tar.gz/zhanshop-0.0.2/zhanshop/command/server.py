import sys

from flask import Flask

from ..helper import Helper
from ..webhandle import WebHandler


class Server():
    app = None
    route = None

    def execute(self, app, route):
        self.app = app
        self.route = route
        self.start()

    def start(self):
        webhandler = WebHandler()
        webhandler.init(self.route)
        webhandler.regRoute(self.app)
        # 开始载入路由
        #app.add_url_rule('/test', 'test', view_func=MyTestClass.as_view("get"))
        #app.run()

    def restart(self):
        pass

    def stop(self):
        pass

    def reload(self):
        pass

    def helper(self):
        pass