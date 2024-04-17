import sys

from flask import Flask

from ..helper import Helper


class Server():
    app = None
    route = None

    def execute(self, app, route):
        self.app = app
        self.route = route
        self.start()

    def start(self):
        pass

    def restart(self):
        pass

    def stop(self):
        pass

    def reload(self):
        pass

    def helper(self):
        pass