<template>
  <div>
    <Table :columns="tableColumn" :data="tableData"></Table>
  </div>
</template>

<script>
export default {
  name: 'TableView',
  // 通过props属性向父组件获取
  props: {
    tableColumn: Array, // 表头，是一个数组
    tableData: Array  // 表数据，也是一个数组
  }
}
</script>

<style>
</style>
