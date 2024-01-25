#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2023/12/29 16:40
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: server.py
# @Software: PyCharm

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
