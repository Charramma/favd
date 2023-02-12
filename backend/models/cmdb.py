from .extension import db
from libs.enums import AssetType, StatusType
from sqlalchemy import func


class Asset(db.Model):
    """资产表"""
    __tablename__ = "asset"
    asset_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    asset_type = db.Column(db.Enum(AssetType), comment="资产类型，服务器或网络设备")
    asset_hostname = db.Column(db.String(64), comment="主机名")
    asset_sn = db.Column(db.String(128), comment="序列号")
    asset_model = db.Column(db.String(64), comment="型号")
    asset_warranty = db.Column(db.DateTime, comment="保修期")
    asset_floor = db.Column(db.Integer, comment="资产所在楼层")
    asset_cabinet_num = db.Column(db.String(32), comment="资产所在机柜")
    asset_cabinet_order = db.Column(db.Integer, comment="资产所在机柜的序号")
    asset_status = db.Column(db.Enum(StatusType),
                             comment="资产当前状态：INIT 初始化;ONLINE 在线;OFFLINE 离线;UNREACHABLE 不可达;MAINTAIN 维修中")
    asset_maintain_record = db.Column(db.Text, comment="维护记录")
    note = db.Column(db.Text, comment="备注")
    create_at = db.Column(db.DateTime, default=func.now(), comment="创建时间")
    update_at = db.Column(db.DateTime, onupdate=func.now(), comment="修改时间")
    status = db.Column(db.Integer)

    manufactory_id = db.Column(db.Integer, db.ForeignKey("manufactory.manufactory_id", ondelete='SET NULL'))
    idc_id = db.Column(db.Integer, db.ForeignKey("idc.idc_id", ondelete="SET NULL"))
    business_unit_id = db.Column(db.Integer, db.ForeignKey("business_unit.business_unit_id", ondelete="SET NULL"))
    user_profile_id = db.Column(db.Integer, db.ForeignKey("user_profile.user_profile_id", ondelete="SET NULL"))
    server_id = db.Column(db.Integer, db.ForeignKey("server.server_id", ondelete="CASCADE"))


class Manufactory(db.Model):
    """厂商表"""
    __tablename__ = "manufactory"
    manufactory_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    manufactory_name = db.Column(db.String(64), comment="厂商名")
    manufactory_tel = db.Column(db.String(11), comment="厂商联系方式")
    note = db.Column(db.Text, comment="备注")
    create_at = db.Column(db.DateTime, default=func.now(), comment="创建时间")
    update_at = db.Column(db.DateTime, onupdate=func.now(), comment="修改时间")
    status = db.Column(db.Integer)

    asset = db.relationship('Asset', backref='manufactory')
    disk = db.relationship('Disk', backref='manufactory')
    memory = db.relationship('Memory', backref='manufactory')


class IDC(db.Model):
    """IDC"""
    __tablename__ = "idc"
    idc_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idc_name = db.Column(db.String(64), comment="idc名")
    idc_name_cn = db.Column(db.String(64), comment="idc中文名称")
    idc_region = db.Column(db.String(64), comment="idc所在区域")
    idc_isp = db.Column(db.String(64), comment="idc供应商")
    note = db.Column(db.Text, comment="备注")
    create_at = db.Column(db.DateTime, default=func.now(), comment="创建时间")
    update_at = db.Column(db.DateTime, onupdate=func.now(), comment="修改时间")
    status = db.Column(db.Integer)

    asset = db.relationship('Asset', backref='idc')


# 业务线表和用户表的中间表
business_unit_user_profile = db.Table('business_unit_user_profile',
                                      db.Column('business_unit_id', db.Integer,
                                                db.ForeignKey('business_unit.business_unit_id'), primary_key=True),
                                      db.Column('user_profile_id', db.Integer,
                                                db.ForeignKey('user_profile.user_profile_id'), primary_key=True)
                                      )


class BusinessUnit(db.Model):
    """业务线表"""
    __tablename__ = "business_unit"
    business_unit_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    business_unit_name = db.Column(db.String(64), comment="业务线名")
    business_unit_name_cn = db.Column(db.String(64), comment="业务线中文名")
    note = db.Column(db.Text, comment="备注")
    create_at = db.Column(db.DateTime, default=func.now(), comment="创建时间")
    update_at = db.Column(db.DateTime, onupdate=func.now(), comment="修改时间")
    status = db.Column(db.Integer)

    asset = db.relationship('Asset', backref='business_unit')
    managers = db.relationship('UserProfile', secondary='business_unit_user_profile',
                               backref='business_units')


class Server(db.Model):
    """服务器表"""
    __tablename__ = "server"
    server_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    server_cpu_count = db.Column(db.Integer, comment="CPU数量")
    server_cpu_core_count = db.Column(db.Integer, comment="CPU核心数")
    server_cpu_model = db.Column(db.String(64), comment="CPU型号")
    server_raid_type = db.Column(db.String(6), comment="服务器raid类型")
    server_ram_size = db.Column(db.Integer, comment="内存大小")
    note = db.Column(db.Text, comment="备注")
    create_at = db.Column(db.DateTime, default=func.now(), comment="创建时间")
    update_at = db.Column(db.DateTime, onupdate=func.now(), comment="修改时间")
    status = db.Column(db.Integer)

    os_id = db.Column(db.Integer, db.ForeignKey("os.os_id"))
    asset = db.relationship('Asset', backref='server', uselist=False)
    nic = db.relationship('Nic', backref='server')
    disk = db.relationship('Disk', backref='server')
    memory = db.relationship('Memory', backref='server')


class Nic(db.Model):
    """网卡表"""
    __tablename__ = "nic"
    nic_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nic_name = db.Column(db.String(12), comment="网卡名")
    nic_model = db.Column(db.String(32), comment="网卡型号")
    nic_ipaddr = db.Column(db.String(17), comment="ip地址")
    nic_mac = db.Column(db.String(17), comment="MAC地址")
    nic_netmask = db.Column(db.String(17), comment="子网掩码")
    note = db.Column(db.Text, comment="备注")
    create_at = db.Column(db.DateTime, default=func.now(), comment="创建时间")
    update_at = db.Column(db.DateTime, onupdate=func.now(), comment="修改时间")
    status = db.Column(db.Integer)

    server_id = db.Column(db.Integer, db.ForeignKey("server.server_id", ondelete='SET NULL'))


class OS(db.Model):
    """操作系统表"""
    __tablename__ = "os"
    os_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    os_type = db.Column(db.String(64), comment="操作系统类型")
    os_version = db.Column(db.String(128), comment="操作系统版本")
    note = db.Column(db.Text, comment="备注")
    create_at = db.Column(db.DateTime, default=func.now(), comment="创建时间")
    update_at = db.Column(db.DateTime, onupdate=func.now(), comment="修改时间")
    status = db.Column(db.Integer)

    server = db.relationship('Server', backref="os")


class Disk(db.Model):
    """硬盘表"""
    __tablename__ = "disk"
    disk_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    disk_sn = db.Column(db.String(128), comment="硬盘序列号")
    disk_slot = db.Column(db.String(10), comment="硬盘插槽")
    disk_model = db.Column(db.String(32), comment="硬盘型号")
    disk_capacity = db.Column(db.String(10), comment="硬盘容量")
    note = db.Column(db.Text, comment="备注")
    create_at = db.Column(db.DateTime, default=func.now(), comment="创建时间")
    update_at = db.Column(db.DateTime, onupdate=func.now(), comment="修改时间")
    status = db.Column(db.Integer)

    manufactory_id = db.Column(db.Integer, db.ForeignKey('manufactory.manufactory_id', ondelete="SET NULL"))
    server_id = db.Column(db.Integer, db.ForeignKey('server.server_id', ondelete="SET NULL"))


class Memory(db.Model):
    """内存条表"""
    __tablename__ = "memory"
    memory_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    memory_sn = db.Column(db.String(128), comment="内存条序列号")
    memory_slot = db.Column(db.String(10), comment="内存条插槽")
    memory_model = db.Column(db.String(32), comment="内存条型号")
    memory_capacity = db.Column(db.String(10), comment="内存大小")
    note = db.Column(db.Text, comment="备注")
    create_at = db.Column(db.DateTime, default=func.now(), comment="创建时间")
    update_at = db.Column(db.DateTime, onupdate=func.now(), comment="修改时间")
    status = db.Column(db.Integer)

    manufactory_id = db.Column(db.Integer, db.ForeignKey('manufactory.manufactory_id', ondelete="SET NULL"))
    server_id = db.Column(db.Integer, db.ForeignKey('server.server_id', ondelete="SET NULL"))
