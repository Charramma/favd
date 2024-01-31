#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2024/1/24 18:26
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: ops_tools_serializer.py
# @Software: PyCharm

from models.ops_tools import FaultInfo
from .extension import ma
from marshmallow import fields
from datetime import datetime


class FaultSchema(ma.Schema):
    class Meta:
        model = FaultInfo
        fields = ('fault_id', 'fault_name', 'fault_status', 'fault_level', 'responsible', 'handler', 'start_time',
                  'end_time', 'cause_of_fault', 'summary_of_fault')

    fault_id = fields.Integer()
    fault_name = fields.String()
    fault_status = fields.String()
    fault_level = fields.String()
    responsible = fields.String()
    handler = fields.String()
    start_time = fields.String()
    end_time = fields.String()
    cause_of_fault = fields.String()
    summary_of_fault = fields.String()

    def post_dump(self, data, many, **kwargs):
        for item in data:
            item['start_time'] = item['start_time'].strftime("%Y-%m-%d %H:%M:%S") if item['start_time'] else None
            item['end_time'] = item['end_time'].strftime("%Y-%m-%d %H:%M:%S") if item['end_time'] else None
        return data




fault_schema = FaultSchema()
faults_schema = FaultSchema(many=True)
