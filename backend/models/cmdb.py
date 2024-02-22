#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2024/2/21 17:59
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: cmdb.py
# @Software: PyCharm

from .extension import db


class IDC(db.Model):
    """IDC"""
    __tablename__ = "idc"
    idc_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idc_name = db.Column(db.String(64), nullable=False, comment="idc名")
    region = db.Column(db.String(64), nullable=False, comment="所属区域")
    idc_supplier = db.Column(db.String(64), nullable=False, comment='供应商')
    administrator = db.Column(db.String(100), nullable=False, comment='管理员')
    administrator_phone = db.Column(db.String(20), nullable=False, comment='管理员电话')
    administrator_email = db.Column(db.String(100), nullable=False, comment='管理员邮箱')
    bandwidth = db.Column(db.String(50), comment='机房带宽')
    ip_address_range = db.Column(db.String(100), nullable=False, comment='IP地址段')
    description = db.Column(db.Text, comment="描述信息")

