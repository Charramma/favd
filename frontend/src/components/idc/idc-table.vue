<template>
  <div>
    <Table border :columns="table_columns" :data="table_data"></Table>
    <Page :model-value="table_page" :total="table_data_count" show-total @on-change="PageChange" style="margin-top: 10px;"></Page>
  </div>
</template>

<script>
  import { mapActions } from 'vuex';

  export default {
    name: 'IdcTable',
    data() {
      return {
        // 表头
        table_columns: [{
            title: 'IDC名称',
            key: 'idc_name',
            align: 'center',
          },
          {
            title: '区域',
            key: 'region',
            align: 'center',
            width: 100
          },
          {
            title: '供应商',
            key: 'idc_supplier',
            align: 'center',
            width: 100
          },
          {
            title: '管理员',
            key: 'administrator',
            align: 'center',
            width: 80
          },
          {
            title: '管理员电话',
            key: 'administrator_phone',
            align: 'center',
            width: 120
          },
          {
            title: '管理员邮箱',
            key: 'administrator_email',
            align: 'center'
          },
          {
            title: '带宽',
            key: 'bandwidth',
            align: 'center',
            width: 100
          },
          {
            title: 'IP地址段',
            key: 'ip_address_range',
            align: 'center'
          },
          {
            title: '描述',
            key: 'description',
            align: 'center',
          },
          {
            title: '操作',
            key: 'action',
            align: 'center',
            width: 150,
            render: (h, params) => {
              return h('div', [
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
                      this.edit(params.index)
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
                      this.del(params.index)
                    }
                  }
                }, '删除')
              ]);
            }
          }
        ],
        table_page: 1
      }
    },
    computed: {
      // 表格数据
      table_data() {
        return this.$store.getters.getIdcTableData;
      },
      // 表格数据量
      table_data_count() {
        return this.$store.getters.getIdcTableDataCount;
      },
      // 表格总页数
      // table_total_page() {
      //   return this.$store.getters.getIdcTableTotalPage;
      // }
    },
    methods: {
      ...mapActions(['handleGetIdcInfo', 'handleDelIdcInfo']),

      // 向后端发送请求获取idc信息
      getIdcInfo(page) {
        this.handleGetIdcInfo(page).then(() => {
          console.log("获取IDC信息成功")
        }).catch(err => {
          this.$Message.error(err);
          console.error("获取IDC信息失败: ", err);
        });
      },
      // 编辑已有idc信息
      edit() {

      },
      // 删除已有idc信息
      del(index) {
        this.$Modal.confirm({
          title: '确定要删除吗？',
          width: '20px',
          onOk: () => {
            this.handleDelIdcInfo(this.table_data[index].idc_id).then(() => {
              this.$Message.success('删除IDC信息成功');
              this.getIdcInfo();
            }).catch(err => {
              this.$Message.error(err);
              console.error('删除IDC信息失败', err);
            })
          }
        })
      },
      // 翻页时调用的方法
      PageChange(page) {
        this.table_page = page;
        this.getIdcInfo(this.table_page);
      }
    },
    mounted() {
      // 挂载组件时调用vuex actions的方法获取idc信息
      this.getIdcInfo(this.table_page);
    }
  }
</script>

<style>
</style>
