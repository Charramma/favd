<template>
  <div class="search-con search-con-top">
    <Select clearable v-model="searchKey" class="search-col" style="width: 200px;">
      <Option v-for="item in searchTypes" :value="item.value" :key="item.value">{{ item.lable }}</Option>
    </Select>
    <Input clearable placeholder="输入关键字搜索" class="search-input" v-model="searchValue" style="width: 200px;" />
    <Button class="search-btn" type="primary">搜索</Button>
    <Button type="success" @click="showModal">新建事件</Button>
  </div>
</template>

<script>
  export default {
    name: 'SearchView',
    data() {
      return {
        searchValue: '', // 搜索关键字
        searchKey: '', // 搜索类别
        searchTypes: [{
            value: 'search_by_eventName',
            lable: '事件名称'
          },
          {
            value: 'search_by_eventStatus',
            lable: '事件状态'
          },
          {
            value: 'search_by_eventLevel',
            lable: '事件级别'
          },
          {
            value: 'search_by_responsible',
            lable: '事件责任人'
          }
        ],
      }
    },
    methods: {
      showModal() {
        this.$emit('showModal', true)
      }
    }
  }
</script>

<style>
  div.search-con-top>* {
    margin-right: 5px;
    margin-bottom: 5px;
  }
</style>
