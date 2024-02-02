<template>
  <div>
    <TableVIew :tableColumn="tableHeader" :tableData="tableData"></TableVIew>
    <Button type="success" @click="openModal">添加新数据</Button>

    <ModalView :visible="showModal" :modalForm="modalForm" @add="addTableData" @change="changeTableData"></ModalView>
  </div>
</template>

<script>
  import axios from 'axios';
  // 引入子组件
  import TableVIew from './Table.vue';
  import ModalView from './Modal.vue';

  export default {
    components: {
      TableVIew,
      ModalView
    },
    data() {
      return {
        // 表头
        tableHeader: [{
            title: 'Name',
            key: 'name'
          },
          {
            title: 'Age',
            key: 'age'
          },
          {
            title: '操作',
            key: 'action',
            width: 150,
            render: (h, params) => {
              return h('div', [
                h('Button', {
                  props: {
                    type: 'primary',
                    size: 'small'
                  },
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: () => {
                      this.editRow(params.index)
                    }
                  }
                }, '编辑'),
                h('Button', {
                  props: {
                    type: 'error',
                    size: 'small'
                  },
                  on: {
                    click: () => {
                      this.delTableData(params.index)
                    }
                  }
                }, '删除')
              ]);
            }
          }
        ],
        tableData: [],    // 表格数据，通过请求后端接口获取
        showModal: false, // 是否展示对话框
        // 对话框内联表单数据
        modalForm: {
          id: '',
          name: '',
          age: ''
        },
      }
    },
    mounted() {
      // 组件挂载时获取表格数据
      this.getTableData();
    },
    methods: {
      // 获取表格数据
      getTableData() {
        // axios.get('http://192.168.5.98:5000/api/v1/test/temps')
        axios.get('http://192.168.0.126:5000/api/v1/test/temps')
          .then(res => {
            this.tableData = res.data.data;
          })
          .catch(err => {
            console.error(err);
          });
      },
      // 新增表格数据
      addTableData(formData) {
        // axios.post('http://192.168.5.98:5000/api/v1/test/temps', formData)
        axios.post('http://192.168.0.126:5000/api/v1/test/temps', formData)
          .then(() => {
            this.showModal = false;
            this.getTableData();
          })
          .catch(err => {
            console.error(err);
          });
      },
      // 修改表格数据
      editRow(index) {
        this.modalForm.id = this.tableData[index].id;
        this.modalForm.name = this.tableData[index].name;
        this.modalForm.age = this.tableData[index].age;
        // this.showModal = true;
        this.openModal();
      },
      changeTableData(formData) {
        const id = formData.id;
        // axios.put(`http://192.168.5.98:5000/api/v1/test/temp/${id}`, formData)
        axios.put(`http://192.168.0.126:5000/api/v1/test/temp/${id}`, formData)
          .then(() => {
            this.showModal = false;
            this.getTableData();
          })
          .catch(err => {
            console.error(err);
          });
      },
      // 删除表格数据
      delTableData(index) {
        const id = this.tableData[index].id;
        axios.delete(`http://192.168.0.126:5000/api/v1/test/temp/${id}`).then(() => {
          this.showModal = false;
          this.getTableData();
        }).catch(err => {
          console.error(err);
        })
      },
      /* Modal的关闭逻辑是隐式的，子组件无法将showModal的值重置为false
         导致页面刷新后第一次打开对话框后，showModal依然是true，无法再次打开对话框
         在这个方法中先将对话框在逻辑上关闭，然后再打开，避免了上面的情况
      */
      openModal() {
        this.showModal = false; // 先重置 showModal 的值为 false
        this.$nextTick(() => {
          this.showModal = true; // 再显示对话框
        });
      }
    }
  }
</script>

<style>
</style>
