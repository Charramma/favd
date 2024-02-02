<template>
  <!-- <Modal v-model="visible" title="添加或修改表格数据"> -->
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
    <div slot="footer">
    </div>
  </Modal>
</template>

<script>
  export default {
    name: 'ModalView',
    props: {
      visible: Boolean, // 对话框是否可见
      modalForm: Object // 对话框内联表单数据
    },
    methods: {
      add() {
        this.$emit('add', this.modalForm);
      },
      change() {
        this.$emit('change', this.modalForm);
      },
      resetForm(name) {
        // this.$emit('reset');
        this.$refs[name].resetFields();
      },
      updateVisible(value) {
        this.$emit('update:visible', value);
      }
    },
  }
</script>

<style>
</style>
