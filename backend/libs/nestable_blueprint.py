from flask import Blueprint


class NestableBlueprint(Blueprint):
    def register_blueprint(self, blueprint, **options):
        def defered(state):
            # 将当前蓝图的 url_prefix 与传入的 blueprint 的 url_prefix 进行拼接，并将拼接后的前缀传给 state.app.register_blueprint 方法。
            # u""  表示空字符串
            url_prefix = (state.url_prefix or u"") +(options.get('url_prefix', blueprint.url_prefix) or u"")
            # 如果 options 中有 url_prefix 值，就将它删除
            if 'url_prefix' in options:
                del options['url_prefix']
            # 将 blueprint 注册到应用中，并使用 url_prefix 和 options 中的其他参数
            state.app.register_blueprint(blueprint, url_prefix=url_prefix, **options)
        # 记录blueprint注册信息
        self.record(defered)
