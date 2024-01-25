#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2023/12/29 17:05
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: extension.py
# @Software: PyCharm


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))

from . import user
from . import ops_tools
