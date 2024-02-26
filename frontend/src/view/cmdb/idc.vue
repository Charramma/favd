<template>
  <div>
    <Card>
      <search-bar></search-bar>
      <idc-table @getIdcData="handleGetIdcData" @ChangePage="HandleChangePage" @delIdcData="handleDelIdc"
        @updateIdcData="getEditableData"></idc-table>
      <modal-view @addIdcData="handleAddIdc" @updateIdcData="handleUpdateIdc"></modal-view>
    </Card>
  </div>
</template>

<script>
  import {
    mapActions
  } from 'vuex';

  import SearchBar from '_c/idc/search-bar.vue';
  import IdcTable from '_c/idc/idc-table.vue';
  import ModalView from '_c/idc/modal.vue';


  export default {
    components: {
      SearchBar,
      IdcTable,
      ModalView
    },
    data() {
      return {

      }
    },
    methods: {
      ...mapActions(['handleGetIdcInfo', 'handleDelIdcInfo', 'handleAddIdcInfo', 'handleUpdateIdcInfo']),

      // 获取表格数据
      handleGetIdcData(page) {
        this.handleGetIdcInfo(page).then(() => {
          console.log("Get IDC info success.");
        }).catch(err => {
          this.$Message.error(err);
          console.error("获取IDC信息失败: ", err);
        });
      },
      // 表格翻页
      HandleChangePage(current_page) {
        this.handleGetIdcData(current_page);
      },
      // 新增一条IDC数据
      handleAddIdc(value) {
        const data = this.$store.getters.getIdcForm;
        this.handleAddIdcInfo(data).then(() => {
          this.$Message.success('添加成功');
          this.handleGetIdcData();
        }).catch(err => {
          this.$Message.error(err);
          console.error("添加IDC信息失败：", err);
        })
      },
      // 删除一条IDC数据
      handleDelIdc(idc_id) {
        const current_page = this.$store.getters.getIdcTableCurrentPage;
        this.handleDelIdcInfo(idc_id).then(() => {
          this.$Message.success('删除IDC信息成功');
          this.handleGetIdcData(current_page);
        }).catch(err => {
          this.$Message.error(err);
          console.error('删除IDC信息失败', err);
        })
      },
      // 获取需要修改idc数据并打开对话框
      getEditableData(idc_info) {
        this.$store.commit('setIdcForm', idc_info); // 用需要修改的数据填充对话框内嵌表单
        this.$store.commit('setIdcModalStatus', true); // 打开对话框
        // this.handleGetIdcData(current_page);
      },
      // 修改一条idc数据
      handleUpdateIdc(idc_info) {
        const current_page = this.$store.getters.getIdcTableCurrentPage;
        this.handleUpdateIdcInfo(idc_info).then(() => {
          this.$Message.success('修改成功');
          this.handleGetIdcData(current_page);
        }).catch(err => {
          this.$Message.error("修改IDC信息失败：", err);
        })
      }
    },
    // 挂载组件时获取一次表格数据
    mounted() {
      this.handleGetIdcData();
    }
  }
</script>

<style>
</style>
