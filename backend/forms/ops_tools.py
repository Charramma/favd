#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2024/1/17 15:36
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: ops_tools.py
# @Software: PyCharm

from wtforms import Form, StringField, DateTimeField, validators, IntegerField
from tools.error_code import FormValidateException
from datetime import datetime


class RandomPassForm(Form):
    character = StringField('character')
    passLength = StringField('passLength')

    def validate_character(self, value):
        character = value.data
        if not character:
            raise FormValidateException(message="至少应该包含一种符号")

    def validate_passLength(self, value):
        pass_length = value.data
        if not pass_length and not pass_length.isdigit():
            raise FormValidateException(message="应该输入一个数字")

        pass_length = int(pass_length)
        if pass_length < 6 or pass_length > 32:
            raise FormValidateException(message="仅支持生成长度为6到32的密码")


class EventInfoForm(Form):
    eventId = StringField()
    eventName = StringField('事件名称')
    eventStatus = StringField('事件状态')
    eventLevel = StringField('事件级别')
    startTime = DateTimeField('事件开始时间', format='%Y-%m-%d %H:%M:%S')
    endTime = DateTimeField('事件结束时间', format='%Y-%m-%d %H:%M:%S')
    handler = StringField('处理人')

    def validate(self, extra_validators=None):
        if not super().validate():
            return False
        else:
            # 开始、结束时间验证
            time_format = '%Y-%m-%d %H:%M:%S'
            current_time = datetime.now()
            if self.startTime.data == 'NaN-NaN-NaN NaN:NaN:NaN': self.startTime.data = ""
            if self.endTime.data == "NaN-NaN-NaN NaN:NaN:NaN": self.endTime.data = ""

            if self.startTime.data and self.endTime.data:   # 如果开始时间和结束时间都有值，开始时间不能晚于结束时间，且均不能晚于当前时间
                start_time = datetime.strptime(self.startTime.data, time_format)
                end_time = datetime.strptime(self.endTime.data, time_format)

                if start_time > end_time:
                    raise FormValidateException(message="开始时间不能晚于结束时间")
                elif start_time > current_time or end_time > current_time:
                    raise FormValidateException(message="开始时间或结束时间不能晚于当前时间")
            elif self.startTime.data and not self.endTime.data: # 如果开始时间存在，结束时间不存在，开始时间不能晚于当前时间
                start_time = datetime.strptime(self.startTime.data, time_format)
                if start_time > current_time:
                    raise FormValidateException(message="开始时间不能晚于当前时间")
            elif not self.startTime.data and self.endTime.data: # 如果开始时间不存在，结束时间存在，不应当出现这种情况
                raise FormValidateException(message="开始时间为空，不能设置结束时间")

            if self.eventStatus.data == '处理中' and self.endTime.data:    # 如果状态还是处理中，不应该有结束时间
                raise FormValidateException(message="事件未关闭，不能设置结束时间")
            elif self.eventStatus.data == '未开始' and self.startTime.data:
                raise FormValidateException(message="事件未开始，不能设置开始时间")

            if not self.eventName.data:
                raise FormValidateException(message="事件名称不能为空")

            if not self.eventStatus.data:
                raise FormValidateException(message="事件状态不能为空")
            elif self.eventStatus.data not in ['未开始', '处理中', '已完成']:
                raise FormValidateException(message="未知的事件状态")

            if not self.eventLevel.data:
                raise FormValidateException(message="事件等级不能为空")
            elif self.eventLevel.data not in ['警告', '严重', '灾难']:
                raise FormValidateException(message="未知的事件等级")

            if not self.handler.data:
                raise FormValidateException(message="事件处理人员、参与人员不可为空")
            return True




class FaultInfoForm(Form):
    faultId = StringField()
    faultName = StringField('故障名称')
    faultStatus = StringField('故障状态')
    faultLevel = StringField('故障级别')
    responsible = StringField('负责人')
    handler = StringField('处理人')  # 可以为空
    startTime = DateTimeField('故障开始时间', format='%Y-%m-%d %H:%M:%S')
    endTime = DateTimeField('故障结束时间', format='%Y-%m-%d %H:%M:%S')  # , validators=[validators.Optional()]
    causeOfFault = StringField('故障原因')  # 可以为空
    summaryOfFault = StringField('故障总结')  # 可以为空

    def validate(self, extra_validators=None):
        if not super().validate():
            return False
        else:
            # 开始、结束时间验证
            time_format = '%Y-%m-%d %H:%M:%S'
            current_time = datetime.now()
            if self.startTime.data == 'NaN-NaN-NaN NaN:NaN:NaN': self.startTime.data = ""
            if self.endTime.data == "NaN-NaN-NaN NaN:NaN:NaN": self.endTime.data = ""

            if self.startTime.data and self.endTime.data:   # 如果开始时间和结束时间都有值，开始时间不能晚于结束时间，且均不能晚于当前时间
                start_time = datetime.strptime(self.startTime.data, time_format)
                end_time = datetime.strptime(self.endTime.data, time_format)

                if start_time > end_time:
                    raise FormValidateException(message="开始时间不能晚于结束时间")
                elif start_time > current_time or end_time > current_time:
                    raise FormValidateException(message="开始时间或结束时间不能晚于当前时间")
            elif self.startTime.data and not self.endTime.data: # 如果开始时间存在，结束时间不存在，开始时间不能晚于当前时间
                start_time = datetime.strptime(self.startTime.data, time_format)
                if start_time > current_time:
                    raise FormValidateException(message="开始时间不能晚于当前时间")
            elif not self.startTime.data and self.endTime.data: # 如果开始时间不存在，结束时间存在，不应当出现这种情况
                raise FormValidateException(message="开始时间为空，不能设置结束时间")

            if self.faultStatus.data == '处理中' and self.endTime.data:    # 如果状态还是处理中，不应该有结束时间
                raise FormValidateException(message="故障未关闭，不能设置结束时间")

            # 故障状态验证
            if not self.faultStatus.data:
                raise FormValidateException(message="故障状态不能为空")
            elif self.faultStatus.data not in ['处理中', '已关闭']:
                raise FormValidateException(message="未知的故障状态")

            # 故障等级验证
            if not self.faultLevel.data:
                raise FormValidateException(message="故障等级不能为空")
            elif self.faultLevel.data not in ['一级故障', '二级故障', '三级故障', '四级故障', '五级故障']:
                raise FormValidateException(message="未知的故障等级")

            # 故障责任人验证
            if not self.responsible.data:
                raise FormValidateException(message="故障责任人不能为空")

            # 故障名称验证
            if not self.faultName.data:
                raise FormValidateException(message="故障名称不能为空")

            return True