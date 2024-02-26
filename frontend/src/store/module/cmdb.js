import {
  getIdcInfo,
  delIdcInfo,
  addIdcInfo,
  updateIdcInfo
} from '@/api/cmdb.js'

export default {
  state: {
    // idc管理
    idc_table_data: [], // idc表格数据
    idc_table_data_count: 0, // idc表格数据量
    idc_table_total_page: '', // idc表格总页数
    idc_table_current_page: 1, // idc表格当前页码
    idc_modal_status: false, // 是否显示idc信息对话框
    idc_search_key: "", // 查询条件
    idc_Form: { // 新增idc信息 对话框内嵌表单
      idc_name: "",
      region: "",
      idc_supplier: "",
      administrator: "",
      administrator_phone: "",
      administrator_email: "",
      bandwidth: "",
      ip_address_range: "",
      description: ""
    }
  },
  getters: {
    getIdcTableData: state => state.idc_table_data,
    getIdcTableDataCount: state => state.idc_table_data_count,
    getIdcTableTotalPage: state => state.idc_table_total_page,
    getIdcTableCurrentPage: state => state.idc_table_current_page,
    getIdcModalStatus: state => state.idc_modal_status,
    getIdcForm: state => state.idc_Form,
    getIdcSearchKey: state => state.idc_search_key
  },
  mutations: {
    setIdcTableData(state, value) {
      state.idc_table_data = value;
    },
    setIdcTableDataCount(state, value) {
      state.idc_table_data_count = value;
    },
    setIdcTableTotalPage(state, value) {
      state.idc_table_total_page = value;
    },
    setIdcTableCurrentPage(state, value) {
      state.idc_table_current_page = value;
    },
    setIdcModalStatus(state, value) {
      state.idc_modal_status = value;
    },
    setIdcForm(state, value) {
      state.idc_Form = value;
    },
    setIdcSearchKey(state, value) {
      state.idc_search_key = value;
    }
  },
  actions: {
    handleGetIdcInfo({
      commit
    }, page) {
      return new Promise((resolve, reject) => {
        getIdcInfo({page}).then(res => {
          const data = res.data;
          commit('setIdcTableData', data.data.idc_info);
          commit('setIdcTableDataCount', data.data.count);
          commit('setIdcTableTotalPage', data.data.total_page);
          resolve();
        }).catch(err => {
          reject(err);
        })
      })
    },
    handleAddIdcInfo({
      commit
    }, idc_info) {
      return new Promise((resolve, reject) => {
        addIdcInfo(idc_info).then(res => {
          const data = res.data;
          resolve();
        }).catch(err => {
          reject(err);
        })
      })
    },
    handleUpdateIdcInfo({
      commit
    }, idc_info) {
      return new Promise((resolve, reject) => {
        updateIdcInfo(idc_info).then(res => {
          const data = res.data;
          resolve();
        }).catch(err => {
          reject(err);
        })
      })
    },
    handleDelIdcInfo({
      commit
    }, idc_id) {
      return new Promise((resolve, reject) => {
        delIdcInfo(idc_id).then(res => {
          const data = res.data;
          resolve();
        }).catch(err => {
          reject(err);
        })
      })
    }
  }
}
