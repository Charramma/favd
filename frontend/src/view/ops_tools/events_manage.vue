<template>
  <div>
    <Card>
      <SearchView @showModal="openModal"></SearchView>
      <table-view :tableHeader="tableHeader" :tableData="tableData" :tablePage="tablePage" :dataCount="tableDataCount"
        @turnPage="handlePageChange"></table-view>
    </Card>

    <ModalView :visible="modalVisible" @getModalData="updateEvent" ref="modalView"></ModalView>
  </div>
</template>

<script>
  import {
    mapActions
  } from 'vuex';
  import ops_tools from '../../store/module/ops_tools';
  import TableView from '_c/events_manage/EventTable.vue';
  import SearchView from '_c/events_manage/SearchBar.vue';
  import ModalView from '_c/events_manage/EventModal.vue';

  export default {
    components: {
      TableView,
      SearchView,
      ModalView
    },
    data() {
      return {
        tableHeader: [{
            title: '事件名称',
            key: 'event_name',
            align: 'center'
          },
          {
            title: '事件状态',
            key: 'event_status',
            align: 'center'
          },
          {
            title: '事件等级',
            key: 'event_level',
            align: 'center'
          },
          {
            title: '处理人',
            key: 'handler',
            align: 'center'
          },
          {
            title: '开始时间',
            key: 'start_time',
            align: 'center'
          },
          {
            title: '结束时间',
            key: 'end_time',
            align: 'center'
          },
          {
            title: '操作',
            key: 'action',
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
                      this.editTableData(params.index)
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
                      this.delTableData(params.index)
                    }
                  }
                }, '删除')
              ]);
            }
          }
        ],
        tableData: [],
        tablePage: 1,
        tableDataCount: "",
        modalVisible: false,
        currentData: {}
      }
    },
    mounted() {
      this.getTableData();
    },
    methods: {
      ...mapActions(['handleGetEvents', 'handleDelEvent', 'handleAddEvent']),
      getTableData() {
        this.handleGetEvents(this.tablePage).then(() => {
          this.tableData = this.$store.getters.getEventsInfo;
          this.tableDataCount = this.$store.getters.getEventCount;
        }).catch(err => {
          this.$Message.error(err);
          console.error("获取故障信息失败: ", err);
        });
      },
      // 翻页
      handlePageChange(page) {
        this.tablePage = page;
        this.getTableData();
      },
      // 删除一条数据
      delTableData(index) {
        this.$Modal.confirm({
          title: '确定要删除吗？',
          width: '20px',
          onOk: () => {
            this.handleDelEvent(this.tableData[index].event_id).then(() => {
              this.$Message.success('删除事件信息成功');
              this.getTableData();
            }).catch(err => {
              this.$Message.error(err);
              console.error('删除事件信息失败', err);
            })
          }
        })
      },
      // editTableData(index) {
      //   const data = {
      //     'eventId': this.tableData[index].event_id,
      //     'eventName': this.tableData[index].event_name,
      //     'eventStatus': this.tableData[index].event_status,
      //     'eventLevel': this.tableData[index].event_level,
      //     'handler': this.tableData[index].handler,
      //     'startTime': this.tableData[index].start_time,
      //     'endTime': this.tableData[index].end_time
      //   }
      //   this.$store.commit('setEventFormData', data);
      //   this.openModal();
      // },
      // 新增或修改数据
      updateEvent(value) {
        if (value.event_id) {
          this.$Message.success('修改成功');
        } else {
          this.handleAddEvent(value).then(() => {
            this.$Message.success('添加新事件成功')
            this.getTableData();
            this.modalVisible = false;
          }).catch(err => {
            this.$Message.error(err);
            console.error('添加新事件失败', err);
          })
        }
      },
      openModal(value) {
        this.modalVisible = false;
        this.$nextTick(() => {
          this.modalVisible = true;
        });
      }
    }
  }
</script>

<style>
</style>
