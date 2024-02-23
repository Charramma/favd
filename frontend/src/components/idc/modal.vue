<template>
  <div>
    <Modal :value='modalStatus' :mask-closable="false" title="IDC信息: " width="550px" class-name="vertical-center-modal">
      <p>lalala</p>

      <!-- 自定义对话框样式 -->
      <div slot="footer"></div> <!-- 禁用默认的确定和取消按钮 -->
      <div slot="close">  <!-- 自定义右上角关闭内容，在关闭时设置vuex中的idc_modal_status为false -->
        <span @click.stop="colseModal"> <!-- @click.stop 阻止事件冒泡，防止默认关闭行为被触发 -->
          <i class="ivu-icon ivu-icon-ios-close"></i> <!-- 关闭图标 × -->
        </span>
      </div>
    </Modal>
  </div>
</template>

<script>
  export default {
    name: 'ModalView',
    computed: {
      // 是否显示对话框
      modalStatus() {
        return this.$store.getters.getIdcModalStatus
      }
    },
    methods: {
      submit() {
        this.$store.commit('setIdcModalStatus', false);
      },
      colseModal() {
        this.$store.commit('setIdcModalStatus', false);
      }
    },
  }
</script>

<style>
  div.search-con-top>* {
    margin-right: 5px;
    margin-bottom: 5px;
  }

  .vertical-center-modal {
    display: flex;
    align-items: center;
    justify-content: center;

    .ivu-modal {
      top: 0;
    }
  }
</style>
