#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2024/1/16 14:51
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: ops_tools.py
# @Software: PyCharm


from tools.nestable_blueprint import NestableBlueprint
from flask_restful import Api, Resource
from flask import current_app, request, jsonify
from tools.response import generate_response
from forms.ops_tools import RandomPassForm, FaultInfoForm, EventInfoForm
from tools.error_code import ArgsTypeException, FormValidateException, DataNotFoundException, Success, \
    DatabaseOperationException
from models.ops_tools import FaultInfo, EventInfo
from models.extension import db
from serializer.ops_tools_serializer import fault_schema, faults_schema, event_schema, events_schema
import string
import random
import math
from datetime import datetime

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

ops_tools_bp = NestableBlueprint('ops_tools_v1', __name__, url_prefix='ops_tools')

api = Api(ops_tools_bp)

# 密钥和偏移量，暂时用固定的
key = b'\x9e\x0c\xed\xf6\x87\x18\x99\xc2E\xb4\x16\x18 \xa5\xe8\x02'
iv = b'\x04\x1d\x14\xea\xc2j\xd2!]R0\xe9\xfe\x1e\xc1\xc1'


class EncryptView(Resource):
    def post(self):
        """aes加密"""
        data = request.json
        if data:
            plain_text = data['plain_text']
            encrypted_data = self.encrypt_aes(plain_text)
            return generate_response(data={'encrypted_data': encrypted_data})
        else:
            raise ValueError

    @staticmethod
    def encrypt_aes(plain_text):
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_data = pad(plain_text.encode('utf-8'), AES.block_size)
        encrypted_data = cipher.encrypt(padded_data)
        cipher_text = base64.b64encode(encrypted_data).decode('utf-8')
        return cipher_text


class DecryptView(Resource):
    def post(self):
        """aes解密"""
        data = request.json
        if data:
            ciphertext = data["ciphertext"]
            decrypted_data = self.decrypt_aes(ciphertext)
            return generate_response(data={'decrypted_data': decrypted_data})
        else:
            raise ValueError

    @staticmethod
    def decrypt_aes(cipher_text):
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_data = base64.b64decode(cipher_text)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size).decode('utf-8')
        return decrypted_data


class RandomPassGenView(Resource):
    def post(self):
        data = request.json
        if not data:
            raise ArgsTypeException(message="参数异常")
        form = RandomPassForm(data=data)
        if form.validate():
            character = form.character.data
            pass_length = form.passLength.data

            random_pass = "".join(random.choices(character, k=int(pass_length)))
            return generate_response(data={"random_pass": random_pass})


# 故障管理
class FaultManageView(Resource):
    def get(self, fault_id):
        """获取单个故障信息"""
        fault = FaultInfo.query.get(fault_id)
        if fault:
            print(type(fault.start_time))
            return generate_response(data=fault_schema.dump(fault))
        else:
            raise DataNotFoundException(message="故障信息不存在")

    def put(self, fault_id):
        """编辑已有故障信息"""
        data = request.json['faultinfo']
        if not data:
            raise ArgsTypeException(message="参数异常")

        form = FaultInfoForm(data=data)
        if form.validate():
            try:
                FaultInfo.change_fault(
                    fault_id=fault_id,
                    fault_name=form.faultName.data,
                    fault_status=form.faultStatus.data,
                    fault_level=form.faultLevel.data,
                    responsible=form.responsible.data,
                    handler=form.handler.data,
                    start_time=form.startTime.data,
                    end_time=form.endTime.data,
                    cause_of_fault=form.causeOfFault.data,
                    summary_of_fault=form.summaryOfFault.data)
                return generate_response(data=fault_schema.dump(FaultInfo.query.get(fault_id)))
            except Exception as e:
                print(e)
                raise DatabaseOperationException(message="修改故障信息失败")
        else:
            result = form.errors
            return jsonify({"message": result})

    def delete(self, fault_id):
        """删除已有故障信息"""
        fault = FaultInfo.query.get(fault_id)
        if fault:
            try:
                db.session.delete(fault)
                db.session.commit()
                return generate_response(message="删除成功", data=fault_schema.dump(fault))
            except Exception as e:
                print(e)
                db.session.rollback()
                raise DatabaseOperationException(message="删除故障信息失败")
        else:
            raise DataNotFoundException(message="故障信息不存在")


class FaultsManageView(Resource):
    def get(self):
        """获取故障信息"""
        page = request.args.get('page', 1, type=int)
        per_page = 10

        # 获取分页数据，一次10条
        faultsinfo = FaultInfo.query.paginate(page=page, per_page=per_page, error_out=False)
        data_count = FaultInfo.query.count()  # 数据总量
        total_page = math.ceil(data_count / per_page)  # 总页码数

        return generate_response(
            data={"faults_info": faults_schema.dump(faultsinfo), "count": data_count, "total_page": total_page})

    def post(self):
        """新增故障信息"""
        data = request.json['faultinfo']

        if not data:
            raise ArgsTypeException(message="参数异常")

        form = FaultInfoForm(data=data)
        if form.validate():
            try:
                FaultInfo.create_fault(
                    fault_name=form.faultName.data,
                    fault_status=form.faultStatus.data,
                    fault_level=form.faultLevel.data,
                    responsible=form.responsible.data,
                    handler=form.handler.data,
                    start_time=form.startTime.data,
                    end_time=form.endTime.data,
                    cause_of_fault=form.causeOfFault.data,
                    summary_of_fault=form.summaryOfFault.data
                )
                return generate_response(data={"message": "提交成功"})
            except Exception as e:
                print(e)
                raise DatabaseOperationException(message="数据插入失败")
        else:
            result = form.errors
            raise DatabaseOperationException(message=result)


# 事件管理
class EventManageView(Resource):
    def get(self, event_id):
        """获取单个事件信息"""
        event = EventInfo.query.get(event_id)
        if event:
            return generate_response(data=event_schema.dump(event))
        else:
            raise DataNotFoundException(message="事件信息不存在")

    def delete(self, event_id):
        """删除单个事件信息"""
        event = EventInfo.query.get(event_id)
        if event:
            try:
                db.session.delete(event)
                db.session.commit()
                return generate_response(message="删除成功", data=fault_schema.dump(event))
            except Exception as e:
                print(e)
                db.session.rollback()
                raise DatabaseOperationException(message="删除事件信息失败")
        else:
            raise DataNotFoundException(message="事件不存在")


class EventsManageView(Resource):
    def get(self):
        """获取所有事件信息"""
        # 当前页码和每页数据量
        page = request.args.get('page', 1, type=int)
        per_page = 10


        # 获取分页数据，一次10条
        events_info = EventInfo.query.paginate(page=page, per_page=per_page, error_out=False)
        data_count = EventInfo.query.count()  # 数据总量
        total_page = math.ceil(data_count / per_page)  # 总页码数

        return generate_response(
            data={"events_info": events_schema.dump(events_info), "count": data_count, "total_page": total_page})

    def post(self):
        """新增事件"""
        data = request.json

        if not data:
            raise ArgsTypeException(message="参数异常")

        form = EventInfoForm(data=data)
        if form.validate():
            try:
                EventInfo.create_event(
                    event_name=form.eventName.data,
                    event_level=form.eventLevel.data,
                    event_status=form.eventStatus.data,
                    handler=form.handler.data,
                    start_time=form.startTime.data,
                    end_time=form.endTime.data
                )
                print('提交成功')
                return generate_response(data={"message": "提交成功"})
            except Exception as e:
                print(e)
                raise DatabaseOperationException(message="数据插入失败")
        else:
            result = form.errors
            raise DatabaseOperationException(message=result)


api.add_resource(EncryptView, '/encrypt')
api.add_resource(DecryptView, '/decrypt')
api.add_resource(RandomPassGenView, '/random_pass')
api.add_resource(FaultsManageView, '/faults')
api.add_resource(FaultManageView, '/fault/<fault_id>')
api.add_resource(EventsManageView, '/events')
api.add_resource(EventManageView, '/event/<event_id>')
