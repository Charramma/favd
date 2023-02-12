from enum import Enum
import datetime


def get_value(obj, key):
    """如果obj为None则直接返回空字符串，如果value为Enum类型则取出它的名字"""
    if obj:
        value = getattr(obj, key)
        if isinstance(value, datetime.datetime):
            return value.strftime("%Y-%m-%d %H:%M:%S")
        return value.name if isinstance(value, Enum) else value
    else:
        return ""


def get_value_list(objlist, *keys):
    """返回一个列表数据"""
    if len(keys) == 0:
        return list()
    else:
        result = list()
        for item in objlist:
            if len(keys) == 1:
                result.append(getattr(item, keys[0]))
            else:
                t_result = {key: getattr(item, key) for key in keys}
                result.append(t_result)
        return result


def get_ip(nics, eth):
    for nic in nics:
        if eth == nic.nic_name:
            return nic.nic_ipaddr
    return ""


def server_item_parse(server):
    # print(server)
    result = {
        "id": server.server_id,
        "os": get_value(server.os, "os_version"),
        "hostname": get_value(server.asset, "asset_hostname"),
        "sn": get_value(server.asset, "asset_sn"),
        "asset_type": get_value(server.asset, "asset_type"),
        "ip": get_ip(server.nic, "eth0"),
        "public_ip": get_ip(server.nic, "eth1"),
        "private_ip": get_ip(server.nic, "eth0"),
        "port": 22,
        "idc": get_value(server.asset.idc, "idc_name_cn"),
        # "admin_user": get_value_list(server.asset.admin.managers, "user_profile_name") if server.asset.admin else [],
        "region": get_value(server.asset.idc, "idc_region"),
        "state": "true",
        "detail": get_value(server, "note"),
        "create_time": get_value(server, "create_at"),
        "update_time": get_value(server, "update_at"),
    }
    return result


def servers_parse(server):
    """"""
    if isinstance(server, list):
        # [<server obj>, <server obj>]
        result = [server_item_parse(item) for item in server]
    else:
        # server = <server obj>
        result = server_item_parse(server)
    return result
