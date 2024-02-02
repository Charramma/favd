<template>
  <!-- 搜索框及新建故障按钮 -->
  <div class="search-con search-con-top">
    <Select clearable v-model="searchKey" class="search-col" style="width: 200px;">
      <Option v-for="item in searchTypes" :value="item.value" :key="item.value">{{ item.lable }}</Option>
    </Select>
    <Input clearable placeholder="输入关键字搜索" class="search-input" v-model="searchValue" style="width: 200px;" />
    <Button class="search-btn" type="primary">搜索</Button>
    <Button type="success" @click="addFault">新建故障信息</Button>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data() {
    return {
      searchValue: '',  // 搜索关键字
      searchKey: '',  // 搜索类别
      searchTypes: [
        { value: 'search_by_faultName', label: '故障名称' },
        { value: 'search_by_faultStatus', label: '故障状态' },
        { value: 'search_by_faultLevel', label: '故障级别' },
        { value: 'search_by_responsible', label: '故障责任人' }
      ]
    };
  },
  methods: {
    addFault() {
      this.$emit('add-fault');
    }
  }
};
</script>

<style>
.search-con-top > * {
  margin-right: 5px;
  margin-bottom: 5px;
}
</style>
