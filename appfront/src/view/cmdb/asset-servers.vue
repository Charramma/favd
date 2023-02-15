<template>
  <div>
    <Card>
      <Alert>这些内容会出现在提示框中</Alert>
      <div class="search">
        <Input v-model="value" placeholder="输入要搜索的内容..." style="width: 200px" />
        <Button :size="buttonSize" type="primary" class="button">搜索</Button>
      </div>
      <div class="table">
        <Table border ref="selection" :columns="table_columns" :data="table_data">
          <!--          <template slot-scope="{row, index}" slot="action">
            <Button type="primary" size="small" style="margin-right: 5px" @click="show(index)">查看</Button>
            <Button type="primary" size="small" style="margin-right: 5px">编辑</Button>
            <Button type="error" size="small" @click="remove(index)">删除</Button>
          </template> -->
        </Table>
        <!-- 实现定义出一个模态框 -->
        <!--       <Modal v-model="modalflag" title="Command Modal dialog box title" @on-ok="ok" @on-cancel="cancel">
          <Input>xxx</Input>
          <Button>xxx</Button>
          <p>Content of dialog</p>
        </Modal> -->
      </div>
    </Card>
  </div>
</template>

<script>
  import {
    getServerList,
    delServer
  } from '../../api/cmdb/servers'
  export default {
    name: 'asset-servers',
    data() {
      return {
        value: '',
        buttonSize: '100px',
        // modalflag为true表示显示模态框，为false表示隐藏模态框
        // modalflag: true,
        table_columns: [{
            type: 'selection',
            width: 60,
            align: 'center'
          },
          {
            title: '主机名',
            // key 直接展示数据
            // key: 'hostname',
            align: 'center',
            sortable: true,
            // render 定制化数据
            render: (h, params) => {
              return h('a', params.row.hostname)
            }
          },
          {
            title: '内网ip',
            key: 'private_ip',
            align: 'center',
            sortable: true
          },
          {
            title: '公网ip',
            key: 'public_ip',
            align: 'center',
            sortable: true
          },
          {
            title: 'IDC',
            key: 'idc',
            align: 'center',
            sortable: true
          },
          {
            title: '区域',
            key: 'region',
            align: 'center',
            sortable: true
          },
          {
            title: '状态',
            // key: 'status',
            align: 'center',
            render: (h, params) => {
              return h('tag', {
                props: {
                  color: 'error'
                }
              }, params.row.state)
            }
          },
          {
            title: '操作',
            key: 'action',
            align: 'center',
            // width: 150,
            // slot: 'action'
            render: (h, params) => {
              return h('div', [
                h('Button', {
                  props: {
                    type: 'success',
                    size: 'small'
                  },
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: () => {
                      this.show(params.index)
                    }
                  }
                }, 'SSH'),
                h('Button', {
                  props: {
                    type: 'primary',
                    size: 'small'
                  },
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: () => {
                      this.show(params.index)
                    }
                  }
                }, '编辑'),
                h('Button', {
                  props: {
                    type: 'error',
                    size: 'small'
                  },
                  on: {
                    click: () => {
                      this.delServer(params.index)
                    }
                  }
                }, '删除')
              ])
            }
          }
        ],
        // 用api提供的数据，就不在此提供了
        table_data: [{
          hostname: 'asdf',
          primaryIp: '192.168.0.10',
          publicIp: '10.10.10.10',
          idc: '阿里云',
          region: '广州',
          status: 'false'
        }]
        // table_data: []
      }
    },
    methods: {
      show(index) {
        this.$Modal.info({
          title: 'User Info',
          content: `Name：${this.table_data[index].name}<br>Age：${this.table_data[index].age}<br>Address：${this.table_data[index].address}`
        })
      },
      remove(index) {
        this.table_data.splice(index, 1);
      },
      ok() {
        // this.modalflag = true
      },
      cancel() {
        console.log("取消")
      },
      // 获取主机列表
      getServerList() {
        // 调用api请求函数
        getServerList().then(res => {
          // 请求成功
          console.log(res.data)
          if (res.data.status_code = 10000) {
            this.table_data = res.data.data
          } else {
            console.log(res.data.message)
          }
        })
      },
      delServer(index) {
        // 找到当前要删除的数据
        // var current_server = this.table_data.splice(index, 1)[0]
        var current_server = this.table_data[index]
        console.log(current_server.id)
        // 在后端删除
        console.log("current_server", current_server)
        delServer(current_server.id)
          .then(
            // 请求成功的处理方式
            res => {
              console.log(res.data)
              if (res.data.status_code = 10000) {
                // 在前端删除table_data数据
                this.table_data.splice(index, 1)
                this.$Message.info(res.data.message);
              } else {
                console.log(res.data.message)
              }
            },
            // 请求失败时的处理方式 => 可省
            res => {
              this.$Message.error("删除主机信息出错了");
            }).catch(
            err => {
              console.log("出错了")
              console.log(err)
              this.$Message.error("删除主机信息出错了");
            })
        // catch 捕获同步异常(与tyr...except功能差不多) => 可省
      },
    },
    mounted() {
      this.getServerList();
    }
  }
</script>

<style lang="less">
  .button {
    margin-left: 5px;
  }

  .search {
    margin-top: 5px;
    margin-bottom: 5px;
  }

  .table {
    margin-top: 5px;
  }
</style>
