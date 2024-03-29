#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2023/12/29 16:54
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: nestable_blueprint.py
# @Software: PyCharm

from flask import Blueprint


class NestableBlueprint(Blueprint):
    def register_blueprint(self, blueprint, **options):
        def defered(state):
            url_prefix = (state.url_prefix or u"") + (options.get('url_prefix', blueprint.url_prefix) or u"")
            if 'url_prefix' in options:
                del options['url_prefix']
            state.app.register_blueprint(blueprint, url_prefix=url_prefix, **options)

        self.record(defered)
