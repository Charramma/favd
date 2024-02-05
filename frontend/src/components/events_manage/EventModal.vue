<template>
  <Modal :value="visible" :mask-closable="false" title="添加或修改事件信息" class-name="vertical-center-modal" width=550px>
    <Form :model="dataForm" :label-width="80" ref="eventModal" :rules="dataFormRule">
      <FormItem label="事件名称: " prop="eventName">
        <Input v-model="dataForm.eventName" placeholder="请输入事件名称"></Input>
      </FormItem>
      <FormItem label="事件状态: " prop="eventStatus">
        <Select v-model="dataForm.eventStatus">
          <Option value="处理中">未开始</Option>
          <Option value="处理中">处理中</Option>
          <Option value="已完成">已完成</Option>
        </Select>
      </FormItem>
      <FormItem label="事件等级: " prop="eventLevel">
        <Select v-model="dataForm.eventLevel">
          <Option value="警告">警告</Option>
          <Option value="严重">严重</Option>
          <Option value="灾难">灾难</Option>
        </Select>
      </FormItem>
      <FormItem label="开始时间" prop="startTime">
        <DatePicker type="datetime" placeholder="选择开始日期和时间" style="width: 400px" v-model="dataForm.startTime"
          format="yyyy-MM-dd HH:mm:ss">
        </DatePicker>
      </FormItem>
      <FormItem label="结束时间" prop="endTime">
        <DatePicker type="datetime" placeholder="选择处理完成日期和时间" style="width: 400px" v-model="dataForm.endTime"
          format="yyyy-MM-dd HH:mm:ss">
        </DatePicker>
      </FormItem>
      <FormItem label="处理人" prop="handler">
        <Input v-model="dataForm.handler" placeholder="处理人"></Input>
      </FormItem>
      <FormItem>
        <Button type="primary" @click="submitForm('eventModal')">提交</Button>
        <Button @click="handleFormReset('eventModal')" style="margin-left: 8px">重置</Button>
      </FormItem>
    </Form>
    <div slot="footer">
      <!-- 此处仅为了禁用默认的确认和取消按钮 -->
    </div>
  </Modal>
</template>

<script>
  export default {
    name: 'ModalView',
    props: {
      visible: Boolean, // 对话框是否可见
    },
    data() {
      return {
        // 表单数据
        dataForm: {
          eventId: "",
          eventName: "",
          eventStatus: "",
          startTime: "",
          endTime: "",
          handler: ""
        },
        // 表单验证规则
        dataFormRule: {
          eventName: [{
            required: true,
            message: '事件名称不能为空',
            trigger: 'blur'
          }],
          eventStatus: [{
            required: true,
            message: '事件状态不能为空',
            trigger: 'blur'
          }],
          eventLevel: [{
            required: true,
            message: '事件等级不能为空',
            trigger: 'blur'
          }],
          handler: [{
            required: true,
            message: '处理人员、参与人员不可为空',
            trigger: 'blur'
          }]
        }
      }
    },
    methods: {
      // 重置表单
      handleFormReset(name) {
        this.$refs[name].resetFields();
      },
      // 日期时间格式转换
      formatDate(dateString) {
        const date = new Date(dateString);
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        const hours = String(date.getHours()).padStart(2, '0');
        const minutes = String(date.getMinutes()).padStart(2, '0');
        const seconds = String(date.getSeconds()).padStart(2, '0');
        return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
      },
      submitForm(name) {
        this.$refs[name].validate((valid) => {
          if (valid) {
            // 将ISO格式的时间转换为本地日期时间格式
            this.dataForm.startTime = this.formatDate(this.dataForm.startTime);
            this.dataForm.endTime = this.formatDate(this.dataForm.endTime);
            this.$emit('getModalData', this.dataForm)
          } else {
            this.$Message.error("缺少必要参数！")
          }
        })
      },

    }
  }
</script>

<style>
  .vertical-center-modal {
    display: flex;
    align-items: center;
    justify-content: center;

    .ivu-modal {
      top: 0;
    }
  }
</style>
