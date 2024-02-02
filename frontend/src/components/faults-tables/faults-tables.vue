<template>
  <div>
    <SearchComponent :search-key="searchKey" :search-value="searchValue" @search-data="handleSearchData">
    </SearchComponent>
    <FaultTable :table-data="tableData" :table-page="tablePage" :table-total="tableTotal"
      @page-change="handlePageChange" @edit-fault-info="handleEditFaultInfo" @del-fault-info="handleDelFaultInfo">
    </FaultTable>
    <AddFaultModal v-model="addFaultModal" :fault-form="addFaultForm" @add-fault-info="handleAddFaultInfo">
    </AddFaultModal>
  </div>
</template>

<script>
  import {
    mapActions,
    mapGetters
  } from 'vuex';
  import ops_tools from '../../store/module/ops_tools';
  import SearchComponent from './SearchComponent.vue';
  import FaultTable from './FaultTable.vue';
  import AddFaultModal from './AddFaultModal.vue';

  export default {
    name: 'FaultsTables',
    components: {
      SearchComponent,
      FaultTable,
      AddFaultModal
    },
    data() {
      return {
        searchKey: '', // 搜索类别
        searchValue: '', // 搜索关键字
        tableData: [], // 表格数据
        tablePage: "1", // 表格页码
        tableTotal: "", // 表格总页码
        addFaultModal: false, // 是否显示新建故障对话框
        addFaultForm: { // 新建故障表单数据
          faultId: "",
          faultName: "", // 故障名称
          faultStatus: "", // 故障状态,
          faultLevel: "", // 故障等级
          responsible: "", // 责任人
          handler: "", // 处理人员
          startTime: "", // 开始时间
          endTime: "", // 结束时间
          causeOfFault: "", // 故障原因
          summaryOfFault: "", //故障总结
        }
      }
    },
    mounted() {
      // 挂载组件时立即获取表格数据
      this.handleTableData();
    },
    methods: {
      ...mapActions([
        'handleAddFault', 'handleGetFaults', 'handleDelFault', 'handleEditFault'
      ]),
      ...mapGetters([
        'getFaultsInfo',
        'getFaultCount'
      ]),
      // 获取表格数据
      handleTableData() {
        this.handleGetFaults(this.tablePage).then(() => {
          this.tableData = this.getFaultsInfo;
          this.tableTotal = this.getFaultCount;
        }).catch(err => {
          this.$Message.error(err);
          console.error("获取故障信息失败: ", err);
        });
      },
      // 搜索数据
      handleSearchData(searchKey, searchValue) {
        this.searchKey = searchKey;
        this.searchValue = searchValue;
        this.handleTableData();
      },
      // 分页器页码改变时触发的方法
      handlePageChange(page) {
        this.tablePage = page;
        this.handleTableData();
      },
      // 编辑故障信息
      handleEditFaultInfo(index) {
        console.log(index)
        this.addFaultModal = true;
      },
      // 删除故障信息
      handleDelFaultInfo(index) {
        console.log(index)
      },
      // 提交新故障信息
      handleAddFaultInfo() {
        console.log('提交')
      }
    },
  }
</script>
