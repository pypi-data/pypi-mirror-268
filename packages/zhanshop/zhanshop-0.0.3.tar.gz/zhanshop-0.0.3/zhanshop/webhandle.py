import importlib
from flask import Blueprint

class WebHandler():
    route = None
    def init(self, route):
        self.route = route
    # 载入路由
    def regRoute(self, app):
        for router in self.route:
            if isinstance(router, Blueprint):
                app.register_blueprint(router)