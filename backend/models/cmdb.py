#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2024/2/21 17:59
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: cmdb.py
# @Software: PyCharm

from .extension import db
from datetime import datetime


# 主机管理
class Host(db.Model):
    __tablename__ = 'hosts'
    host_id = db.Column(db.Integer, primary_key=True, name='host_id', autoincrement=True)
    hostname = db.Column(db.String(100), nullable=False, name='hostname', comment='主机名')
    intranet_ip = db.Column(db.String(32), nullable=False, name='intranet_ip', comment='内网IP')
    internet_ip = db.Column(db.String(32), nullable=True, name='internet_ip', comment='公网IP')
    idc_id = db.Column(db.Integer, db.ForeignKey('idcs.id'), nullable=False)  # 添加外键引用IDC表的ID字段
    region = db.Column(db.String(50), nullable=False, name='region', comment='所属区域')
    status = db.Column(db.String(20), nullable=False, name='status', comment='状态')


# IDC管理
class IDC(db.Model):
    __tablename__ = 'idcs'
    id = db.Column(db.Integer, primary_key=True, name='idc_id', autoincrement=True)
    name = db.Column(db.String(100), nullable=False, name='name', comment='idc名称')
    admin = db.Column(db.String(50), name='admin', comment='管理员姓名')
    email = db.Column(db.String(100), name='email', comment='管理员邮箱')
    phone = db.Column(db.String(20), name='phone', comment='管理员电话')
    address = db.Column(db.String(200), name='address', comment='idc地址')
    network_type = db.Column(db.String(50), name='network_type', comment='机房网络类型')
    bandwidth = db.Column(db.Float, name='bandwidth', comment='机房带宽')
    ip_address_range = db.Column(db.String(100), name='ip_address_range', comment='IP地址段')
    description = db.Column(db.Text, name='description', comment='描述信息')

    hosts = db.relationship('Host', backref='idc_info', lazy=True)  # 建立一对多关系，一个IDC可以有多个Host