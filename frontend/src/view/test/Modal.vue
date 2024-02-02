<template>
  <Modal :value="visible" title="添加或修改表格数据">
    <Form :model="modalForm" :label-width="80" ref="modalForm">
      <FormItem label="Name: " prop="name">
        <Input v-model="modalForm.name"></Input>
      </FormItem>
      <FormItem label="Age: " prop="age">
        <Input v-model="modalForm.age"></Input>
      </FormItem>
      <FormItem>
        <Button type="primary" @click="add">添加数据</Button>
        <Button type="primary" @click="change">修改数据</Button>
        <Button @click="resetForm('modalForm')" style="margin-left: 8px">重置</Button>
      </FormItem>
    </Form>
    <div slot="footer"></div> <!-- 此处仅为了禁用默认的底部按钮 -->
  </Modal>
</template>

<script>
  export default {
    name: 'ModalView',
    // props的数据从父组件获取
    props: {
      visible: Boolean, // 对话框是否可见
      modalForm: Object // 对话框内联表单数据
    },
    methods: {
      // 新增一条数据
      add() {
        // 父组件触发自定义的add事件，通过$emit将this.modalForm的数据发送给父组件
        this.$emit('add', this.modalForm);
      },
      // 修改一条数据
      change() {
        // 父组件触发自定义的change事件，通过$emit将this.modalForm的数据发送给父组件
        this.$emit('change', this.modalForm);
      },
      // 重置（清空）表单
      resetForm(name) {
        this.$refs[name].resetFields();
      }
    },
  }
</script>

<style>
</style>
