#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2024/2/22 17:39
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: cmdb.py
# @Software: PyCharm

from tools.nestable_blueprint import NestableBlueprint
from flask_restful import Api, Resource
from flask import current_app, request, jsonify
from tools.response import generate_response
from models.extension import db
from models.cmdb import IDC
from serializer.cmdb_serializer import idc_schema, idcs_schema
from forms.cmdb import IDCForm
from tools.error_code import DataNotFoundException, DatabaseOperationException, ArgsTypeException, FormValidateException

cmdb_bp = NestableBlueprint('cmdb_v1', __name__, url_prefix='cmdb')
api = Api(cmdb_bp)


class IdcView(Resource):
    def get(self, idc_id):
        """根据id获取单条idc信息"""
        idc = IDC.query.get(idc_id)
        if idc:
            return generate_response(data=idc_schema.dump(idc))
        else:
            raise DataNotFoundException(message="IDC信息不存在")

    def put(self, idc_id):
        """编辑已有idc信息"""
        pass

    def delete(self, idc_id):
        """根据id删除指定idc信息"""
        idc = IDC.query.get(idc_id)
        if idc:
            try:
                db.session.delete(idc)
                db.session.commit()
                return generate_response(message="删除成功", data=idc_schema.dump(idc))
            except Exception as e:
                print(e)
                db.session.rollback()
                raise DatabaseOperationException(message="删除IDC信息失败")
        else:
            raise DataNotFoundException(message="IDC信息不存在")


class IdcsView(Resource):
    def get(self):
        """获取所有idc信息"""
        idcs = IDC.query.all()
        return generate_response(idcs_schema.dump(idcs))

    def post(self):
        data = request.json

        if not data:
            raise ArgsTypeException(message="参数异常")

        form = IDCForm(data=data)
        if form.validate():
            idc = IDC(
                idc_name=form.idc_name.data,
                region=form.region.data,
                idc_supplier=form.idc_supplier.data,
                administrator=form.administrator.data,
                administrator_phone=form.administrator_phone.data,
                administrator_email=form.administrator_email.data,
                bandwidth=form.bandwidth.data,
                ip_address_range=form.ip_address_range.data,
                description=form.description.data
            )
            try:
                db.session.add(idc)
                db.session.commit()
                return generate_response(message="添加成功", data=idc_schema.dump(idc))
            except Exception as e:
                print(e)
                db.session.rollback()
                raise DatabaseOperationException(message="新增IDC信息失败")
        else:
            result = form.errors
            raise FormValidateException(message=result)




api.add_resource(IdcView, '/idc/<idc_id>')
api.add_resource(IdcsView, '/idc')