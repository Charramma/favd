<template>
  <div class="search-con search-con-top">
    <Input v-model="search_key" clearable placeholder="输入IDC名称关键字搜索" class="search-input" style="width: 200px;" />
    <Button class="search-btn" type="primary" @click="search">搜索</Button>
    <Button type="success" @click="openModal">新建IDC</Button>
  </div>
</template>

<script>
  export default {
    name: 'SearchBar',
    data() {
      return {
        search_key: ""
      }
    },
    methods: {
      // 搜索
      search() {
        this.$emit('searchIdc', this.search_key);
      },
      // 新建IDC
      openModal() {
        this.$store.commit('setIdcForm', {}); // 通过新建IDC按钮打开对话框前，先清空对话框
        this.$store.commit('setIdcModalStatus', true);
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
