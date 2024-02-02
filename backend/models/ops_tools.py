#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2024/1/23 18:16
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: ops_tools.py
# @Software: PyCharm

from .extension import db
from datetime import datetime


class EventInfo(db.Model):
    """事件管理-事件信息"""
    __tablename__ = "event_info"
    event_id = db.Column(db.Integer, primary_key=True, name='event_id', autoincrement=True)
    event_name = db.Column(db.String(255), nullable=False, name='event_name', comment='事件名称')
    event_status = db.Column(db.String(50), nullable=False, name='event_status', comment='事件状态')
    event_level = db.Column(db.String(50), nullable=False, name='event_level', comment='事件等级')
    handler = db.Column(db.String(255), nullable=False, name='handler', comment='事件处理人')
    start_time = db.Column(db.DateTime, nullable=True, name='start_time', comment="开始时间")
    end_time = db.Column(db.DateTime, nullable=True, name='end_time', comment="结束时间")

    @classmethod
    def create_event(cls, event_name, event_status, event_level, handler, start_time, end_time):
        event = cls()
        event.event_name = event_name
        event.event_status = event_status
        event.event_level = event_level
        event.handler = handler

        if start_time:
            start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
            event.start_time = start_time

        if end_time:
            end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
            event.end_time = end_time

    @classmethod
    def change_event(cls, event_id, event_name, event_status, event_level, handler, start_time, end_time):
        event = cls().query.get(event_id)
        event.event_name = event_name
        event.event_status = event_status
        event.event_level = event_level
        event.handler = handler

        if start_time:
            start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
            event.start_time = start_time

        if end_time:
            end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
            event.end_time = end_time


class FaultInfo(db.Model):
    """故障管理-故障信息"""
    __tablename__ = "fault_info"
    fault_id = db.Column(db.Integer, primary_key=True, name='fault_id', autoincrement=True)
    fault_name = db.Column(db.String(255), nullable=False, name='fault_name', comment="故障名称")
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
        fault.fault_name = fault_name
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
        try:
            db.session.add(fault)
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    @classmethod
    def change_fault(cls, fault_id, fault_name, fault_status, fault_level, responsible, handler, start_time, end_time,
                     cause_of_fault, summary_of_fault):
        """修改故障信息时调用该函数，需要对日期格式进行处理"""
        fault = cls().query.get(fault_id)
        fault.fault_name = fault_name
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
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
