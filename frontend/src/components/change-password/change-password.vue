<template>
  <Card>
    <h1 style="margin-bottom: 10px;">修改密码</h1>
    <Form ref="changePasswordForm" :model="form" :rules="rules" style="width: 300px" label-width='80'>
      <FormItem prop="old_password" label="当前密码">
        <Input type="password" v-model="form.old_password" placeholder="请输入当前密码" maxlength='16'></Input>
      </FormItem>
      <FormItem prop="new_password" label="新密码">
        <Input type="password" v-model="form.new_password" placeholder="请输入新密码" maxlength='16'></Input>
      </FormItem>
      <FormItem prop="new_password_check" label="确认新密码">
        <Input type="password" v-model="form.new_password_check" placeholder="请再次输入新密码" maxlength='16'></Input>
      </FormItem>
      <FormItem style="width: 200px;">
        <Button @click="handleSubmit('changePasswordForm')" type="primary" long>提交</Button>
      </FormItem>
    </Form>
  </Card>
</template>

<script>
  export default {
    name: 'ChangePassword',
    props: {
      oldPasswordRules: {
        type: Array,
        default: () => {
          return [{
            required: true,
            message: '旧密码不能为空',
            trigger: 'blur'
          }]
        }
      },
      newPasswordRules: {
        type: Array,
        default: () => {
          return [{
              required: true,
              message: '新密码不能为空',
              trigger: 'blur'
            },
            {
              min: 8,
              message: '新密码长度不能少于8位',
              trigger: 'blur'
            },
            {
              pattern: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]+$/,
              message: '密码必须包含大小写字母、数字和特殊符号',
              trigger: 'blur'
            }
          ]
        }
      },
      newPasswordCheckRules: {
        type: Array,
        default: () => {
          return [{
            required: true,
            message: '请再次输入新密码',
            trigger: 'blur'
          }]
        }
      }
    },
    data() {
      return {
        form: {
          old_password: '',
          new_password: '',
          new_password_check: ''
        }
      }
    },
    computed: {
      rules() {
        return {
          old_password: this.oldPasswordRules,
          new_password: this.newPasswordRules,
          new_password_check: [
            ...this.newPasswordCheckRules,
            {
              validator: this.validateNewPasswordCheck,
              trigger: ['blur', 'change']
            }
          ]
        }
      }
    },
    methods: {
      handleSubmit() {

      },
      // 检测二次输入的密码是否正确
      validateNewPasswordCheck(rule, value, callback) {
        if (value !== this.form.new_password) {
          callback(new Error('两次输入的密码不一致'));
        } else {
          callback();
        }
      }
    }
  }
</script>

<style>
</style>
