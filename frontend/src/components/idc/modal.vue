<template>
  <div>
    <Modal :value='modalStatus' :mask-closable="false" title="IDC信息: " width="550px" class-name="vertical-center-modal">
      <Form :model='idcForm' :label-width="100" ref="idcForm" :rules="idcValidate">
        <FormItem label="IDC名称" prop="idc_name">
          <Input v-model="idcForm.idc_name" placeholder="请输入IDC的名称"></Input>
        </FormItem>
        <FormItem label="所属区域" prop='region'>
          <Input v-model="idcForm.region" placeholder="请输入IDC所属区域"></Input>
        </FormItem>
        <FormItem label="供应商" prop='idc_supplier'>
          <Input v-model="idcForm.idc_supplier" placeholder="请输入IDC的供应商"></Input>
        </FormItem>
        <FormItem label="管理员" prop='administrator'>
          <Input v-model="idcForm.administrator" placeholder="请输入IDC管理员姓名"></Input>
        </FormItem>
        <FormItem label="管理员电话" prop='administrator_phone'>
          <Input v-model="idcForm.administrator_phone" placeholder="请输入11位电话号码"></Input>
        </FormItem>
        <FormItem label="管理员邮箱" prop='administrator_email'>
          <Input v-model="idcForm.administrator_email" placeholder="请输入IDC管理员邮箱地址"></Input>
        </FormItem>
        <FormItem label="机房带宽" prop='bandwidth'>
          <Input v-model="idcForm.bandwidth" placeholder="请输入IDC机房带宽"></Input>
        </FormItem>
        <FormItem label="IP地址段" prop='ip_address_range'>
          <Input v-model="idcForm.ip_address_range" placeholder="请输入机房网络IP地址段"></Input>
        </FormItem>
        <FormItem label="描述信息" prop='description'>
          <Input v-model="idcForm.description" type="textarea" :autosize="{minRows: 2,maxRows: 5}"></Input>
        </FormItem>
        <FormItem>
          <Button type="primary" @click="submit('idcForm')">提交</Button>
          <Button style="margin-left: 8px" @click="resetForm('idcForm')">重置</Button>
        </FormItem>
      </Form>

      <!-- 自定义对话框样式 -->
      <div slot="footer"></div> <!-- 禁用默认的确定和取消按钮 -->
      <div slot="close"> <!-- 自定义右上角关闭内容，在关闭时设置vuex中的idc_modal_status为false -->
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
    data() {
      return {
        // 表单验证规则
        idcValidate: {
          idc_name: [{
            required: true,
            message: 'IDC名称不能为空',
            trigger: 'blur'
          }],
          region: [{
            required: true,
            message: 'IDC所属区域不能为空',
            trigger: 'blur'
          }],
          idc_supplier: [{
            required: true,
            message: 'IDC供应商不能为空',
            trigger: 'blur'
          }],
          administrator: [{
            required: true,
            message: 'IDC管理员不能为空',
            trigger: 'blur'
          }],
          administrator_phone: [{
            required: true,
            message: 'IDC管理员电话不能为空',
            trigger: 'blur'
          }, ],
          administrator_email: [{
              required: true,
              message: 'IDC管理员邮箱不能为空',
              trigger: 'blur'
            },
            {
              type: 'email',
              message: '邮箱格式异常',
              trigger: 'blur'
            }
          ],
          ip_address_range: [{
            required: true,
            message: 'IP网络地址段不能为空',
            trigger: 'blur'
          }]
        }
      }
    },
    computed: {
      // 是否显示对话框
      modalStatus() {
        return this.$store.getters.getIdcModalStatus;
      },
      idcForm() {
        return this.$store.getters.getIdcForm;
      }
    },
    methods: {
      submit(name) {
        this.$refs[name].validate((valid) => { // 对表单进行验证
          if (valid) { // 表单验证通过
            this.$store.commit('setIdcForm', this.idcForm);
            if (this.idcForm.idc_id) { // 如果存在idc_id，说明这是修改数据
              this.$emit('updateIdcData', this.idcForm);
            } else { // 没有idc_id，是新增数据
              this.$emit('addIdcData', this.idcForm);
            }
            this.colseModal(); // 关闭对话框
          } else {
            this.$Message.error('表单数据不合法！');
          }
        })
      },
      // 关闭对话框
      colseModal() {
        this.$store.commit('setIdcModalStatus', false);
      },
      // 重置对话框内置表单
      resetForm(name) {
        this.$refs[name].resetFields();
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
