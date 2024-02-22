#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2024/2/22 17:47
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: cmdb_serializer.py
# @Software: PyCharm

from .extension import ma
from models.cmdb import IDC


class IDCSchema(ma.Schema):
    class Meta:
        model = IDC
        fields = ('idc_id','idc_name','region','idc_supplier','administrator','administrator_phone','administrator_email','bandwidth','ip_address_range','description')


idc_schema = IDCSchema()
idcs_schema = IDCSchema(many=True)