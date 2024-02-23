<template>
  <div class="search-con search-con-top">
    <Input clearable placeholder="输入关键字搜索" class="search-input" style="width: 200px;" />
    <Button class="search-btn" type="primary">搜索</Button>
    <Button type="success" @click="openModal">新建IDC</Button>
  </div>
</template>

<script>
  export default {
    name: 'SearchBar',
    methods: {
      openModal() {
        this.$store.commit('setIdcModalStatus', true)
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
