#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2024/1/23 18:16
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: ops_tools.py
# @Software: PyCharm

from .extension import db
from datetime import datetime


class FaultInfo(db.Model):
    """故障管理-故障信息"""
    __tablename__ = "fault_info"
    fault_id = db.Column(db.Integer, primary_key=True, name='fault_id', autoincrement=True)
    falut_name = db.Column(db.String(255), nullable=False, name='falut_name', comment="故障名称")
    fault_status = db.Column(db.String(20), nullable=False, name='fault_status', comment="故障状态")
    fault_level = db.Column(db.String(20), nullable=False, name='fault_level', comment="故障等级")
    responsible = db.Column(db.String(255), nullable=False, name='responsible', comment="责任人")
    handler = db.Column(db.String(255), nullable=True, name='handler', comment="处理人")
    start_time = db.Column(db.DateTime, nullable=True, name='start_time', comment="开始时间")
    end_time = db.Column(db.DateTime, nullable=True, name='end_time', comment="结束时间")
    cause_of_fault = db.Column(db.String(2048), nullable=True, name='cause_of_fault', comment="故障原因")
    summary_of_fault = db.Column(db.String(2048), nullable=True, name='summary_of_fault', comment="故障总结")

    @classmethod
    def create_fault(cls, fault_name, fault_status, fault_level, responsible, handler, start_time, end_time,
                     cause_of_fault, summary_of_fault):
        fault = cls()
        fault.falut_name = fault_name
        fault.fault_status = fault_status
        fault.fault_level = fault_level
        fault.responsible = responsible
        fault.handler = handler
        fault.cause_of_fault = cause_of_fault
        fault.summary_of_fault = summary_of_fault

        if start_time:
            start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
            fault.start_time = start_time

        if end_time:
            end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
            fault.end_time = end_time

        db.session.add(fault)
        db.session.commit()
