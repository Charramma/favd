<template>
  <div>
    <Table :columns="tableHeader" :data="tableData"></Table>
    <Page :model-value="tablePage" :total="dataCount" show-total @on-change="handlePageChange"
      style="margin-top: 10px;"></Page>
  </div>
</template>

<script>
export default {
  name: 'TableView',
  props: {
    tableHeader: Array, // 表头
    tableData: Array  , // 表数据
    tablePage: Number,  // 当前页码
    dataCount: Number   // 表总数据量
  },
  methods: {
    handlePageChange(page) {
      this.$emit('turnPage', page)
    }
  }
}
</script>

<style>
</style>
