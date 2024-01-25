#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2024/1/24 18:26
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: ops_tools_serializer.py
# @Software: PyCharm

from models.ops_tools import FaultInfo
from .extension import ma


class FaultSchema(ma.Schema):
    class Meta:
        model = FaultInfo
        fields = ('fault_id', 'falut_name', 'fault_status', 'fault_level', 'responsible', 'handler', 'start_time',
                  'end_time', 'cause_of_faul', 'summary_of_fault')


fault_schema = FaultSchema()
faults_schema = FaultSchema(many=True)
