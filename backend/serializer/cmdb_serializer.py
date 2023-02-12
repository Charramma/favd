from .extension import ma
from models.cmdb import Server


class ServerSchema(ma.Schema):
    class Meta:
        models = Server
        fields = ("server_id", "server_cpu_count", "server_cpu_core_count", "server_cpu_model", "server_raid_type",
                  "server_ram_size", "note", "create_at", "update_at", "status", "os_id")


server_schema = ServerSchema()
servers_schema = ServerSchema(many=True)
