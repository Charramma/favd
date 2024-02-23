<template>
  <div>
    <Card>
      <search-bar></search-bar>
      <idc-table></idc-table>
      <modal-view></modal-view>
    </Card>
  </div>
</template>

<script>
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

    },

  }
</script>

<style>
</style>
