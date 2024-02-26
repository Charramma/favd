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
from sqlalchemy import or_
from models.cmdb import IDC
from serializer.cmdb_serializer import idc_schema, idcs_schema
from forms.cmdb import IDCForm
from tools.error_code import DataNotFoundException, DatabaseOperationException, ArgsTypeException, FormValidateException
import math

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
        data = request.json
        if not data:
            raise ArgsTypeException(message="参数异常")
        form = IDCForm(data=data)
        if form.validate():
            try:
                idc = IDC.query.get(idc_id)
                print(idc)
                idc.idc_name = form.idc_name.data
                idc.region = form.region.data
                idc.idc_supplier = form.idc_supplier.data
                idc.administrator = form.administrator.data
                idc.administrator_phone = form.administrator_phone.data
                idc.administrator_email = form.administrator_email.data
                idc.bandwidth = form.bandwidth.data
                idc.ip_address_range = form.ip_address_range.data
                idc.description = form.description.data
                db.session.commit()
                return generate_response(message="修改IDC信息成功")
            except Exception as e:
                print(e)
                db.session.rollback()
                raise DatabaseOperationException(message="修改IDC信息失败")
        else:
            result = form.errors
            raise FormValidateException(message=result)


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
        # 当前页码和每页显示的数据条数
        page = request.args.get('page', 1, type=int)
        per_page = 10

        # 查询关键字（对idc_name进行模糊查询)
        key = request.args.get('key', '', type=str)

        query = IDC.query

        # 如果存在查询条件，对idc_name进行模糊查询
        if key:
            query = query.filter(or_(IDC.idc_name.like(f'%{key}%'), IDC.idc_name.ilike(f'%{key}%')))

        # 获取分页数据，一次10条
        idc_info = query.paginate(page=page, per_page=per_page, error_out=False)
        count = IDC.query.count()  # 数据总量
        total_page = math.ceil(count/per_page)  # 总页码

        return generate_response(data={"idc_info": idcs_schema.dump(idc_info), "count": count, "total_page": total_page})

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
