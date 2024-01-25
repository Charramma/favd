#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2023/12/29 16:46
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: views.py
# @Software: PyCharm

from flask import Blueprint, jsonify

bp = Blueprint("bp", __name__, url_prefix='/')


@bp.route('/checkhealth', methods=['GET'])
def check_health():
    """ 检测后端是否正常运行 """
    response_data = {"code": 200, "message": "It's ok!"}
    return jsonify(response_data)