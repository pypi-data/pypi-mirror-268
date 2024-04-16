class WebHandler():
    route = None
    def init(self, route):
        self.route = route
    # 载入路由
    def regRoute(self, app):
        attributes = dir(self.route)
        for item in attributes:
            if "__" not in item:
                routes = getattr(self.route, item)
                # 开始遍历数组
                for route in routes:
                    app.add_url_rule(rule=route[0], view_func=route[1], methods=route[2])