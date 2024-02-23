import {
  getIdcInfo,
  delIdcInfo
} from '@/api/cmdb.js'

export default {
  state: {
    // idc管理
    idc_table_data: [], // idc表格数据
    idc_table_data_count: '', // idc表格数据量
    idc_table_total_page: '', // idc表格总页数
    idc_modal_status: false  // 是否显示idc信息对话框
  },
  getters: {
    getIdcTableData: state => state.idc_table_data,
    getIdcTableDataCount: state => state.idc_table_data_count,
    getIdcTableTotalPage: state => state.idc_table_total_page,
    getIdcModalStatus: state => state.idc_modal_status
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
    setIdcModalStatus(state, value) {
      state.idc_modal_status = value;
    }
  },
  actions: {
    handleGetIdcInfo({commit}, page) {
      return new Promise((resolve, reject) => {
        getIdcInfo({page}).then(res => {
          const data = res.data;
          commit('setIdcTableData', data.data.idc_info);
          commit('setIdcTableDataCount', data.data.count);
          commit('getIdcTableTotalPage', data.data.total_page);
          resolve();
        }).catch(err => {
          reject(err);
        })
      })
    },
    handleDelIdcInfo({commit}, idc_id) {
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
