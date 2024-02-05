import {
  encrypt,
  decrypt,
  randomPassGen,
  addFault,
  getFaults,
  delFault,
  editFault,
  getEvents,
  delEvent,
  addEvent
} from '@/api/ops_tools.js'

export default {
  state: {
    plain_text: "",
    ciphertext: "",
    random_pass: "",
    /* 故障管理 */
    faultsInfo: [], // 所有故障信息
    faultCount: "", // 总故障数
    faultTotalPage: "" ,// 总页数
    /* 事件管理 */
    eventsInfo: [], // 所有事件信息
    eventCount: "", // 总事件数
    eventTotalPage: "",  // 总页数
  },
  mutations: {
    setCipherText(state, ciphertext) {
      state.ciphertext = ciphertext
    },
    setPlainText(state, plain_text) {
      state.plain_text = plain_text
    },
    setRandomPass(state, random_pass) {
      state.random_pass = random_pass
    },
    setFaultsInfo(state, faultsInfo) {
      state.faultsInfo = faultsInfo;
    },
    setFaultCount(state, faultCount) {
      state.faultCount = faultCount;
    },
    setFaultTotalPage(state, faultTotalPage) {
      state.faultTotalPage = faultTotalPage
    },
    setEventsInfo(state, eventsInfo) {
      state.eventsInfo = eventsInfo;
    },
    setEventCount(state, eventCount) {
      state.eventCount = eventCount;
    },
    setEventTotalPage(state, eventTotalPage) {
      state.eventTotalPage = eventTotalPage;
    },
  },
  getters: {
    getCiphertext: state => state.ciphertext,
    getPlaintext: state => state.plain_text,
    getRandompass: state => state.random_pass,
    getFaultCount: state => state.faultCount,
    getFaultTotalPage: state => state.faultTotalPage,
    getFaultsInfo: state => state.faultsInfo,
    getEventCount: state => state.eventCount,
    getEventTotalPage: state => state.eventTotalPage,
    getEventsInfo: state => state.eventsInfo
  },
  actions: {
    handleEncrypt({
      commit
    }, plain_text) {
      // plain_text = plain_text.trim();
      return new Promise((resolve, reject) => {
        encrypt({
            plain_text
          })
          .then(res => {
            const data = res.data;
            commit('setCipherText', data.data.encrypted_data);
            //
            console.log(data.data.encrypted_data)
            resolve();
          })
          .catch(err => {
            reject(err);
          });
      });
    },
    handleDecrypt({
      commit
    }, ciphertext) {
      return new Promise((resolve, reject) => {
        decrypt({
          ciphertext
        }).then(res => {
          const data = res.data;
          commit('setPlainText', data.data.decrypted_data)
          resolve();
        }).catch(err => {
          reject(err);
        })
      })
    },
    handleRandomPassGen({
      commit
    }, {
      character,
      passLength
    }) {
      return new Promise((resolve, reject) => {
        randomPassGen({
          character,
          passLength
        }).then(res => {
          const data = res.data;
          commit('setRandomPass', data.data.random_pass);
          resolve();
        }).catch(err => {
          reject(err.response.data.message);
        })
      })
    },
    // 新增故障信息
    handleAddFault({
      commit
    }, faultinfo) {
      return new Promise((resolve, reject) => {
        addFault({
          faultinfo
        }).then(res => {
          const data = res.data;
          resolve();
        }).catch(err => {
          reject(err);
        })
      })
    },
    // 编辑已有故障信息
    handleEditFault({
      commit
    }, faultinfo) {
      return new Promise((resolve, reject) => {
        editFault({
          faultinfo
        }).then(res => {
          const data = res.data;
          resolve();
        }).catch(err => {
          reject(err);
        })
      })
    },
    // 获取所有故障信息
    handleGetFaults({
      commit
    }, page) {
      return new Promise((resolve, reject) => {
        getFaults({
          page
        }).then(res => {
          const data = res.data;
          commit('setFaultsInfo', data.data.faults_info);
          commit('setFaultTotalPage', data.data.total_page);
          commit('setFaultCount', data.data.count);
          resolve();
        }).catch(err => {
          reject(err);
        })
      })
    },
    // 根据fault_id删除故障信息
    handleDelFault({
      commit
    }, fault_id) {
      return new Promise((resolve, reject) => {
        delFault(fault_id).then(res => {
          const data = res.data;
          resolve();
        }).catch(err => {
          reject(err);
        })
      })
    },
    /*
    * 事件管理
    */
    // 获取所有事件信息
    handleGetEvents({
      commit
    }, page) {
      return new Promise((resolve, reject) => {
        getEvents({
          page
        }).then(res => {
          const data = res.data;
          commit('setEventsInfo', data.data.events_info);
          commit('setEventTotalPage', data.data.total_page);
          commit('setEventCount', data.data.count);
          resolve();
        }).catch(err => {
          reject(err);
        })
      })
    },
    // 根据event_id删除故障信息
    handleDelEvent({
      commit
    }, event_id) {
      return new Promise((resolve, reject) => {
        delEvent(event_id).then(res => {
          const data = res.data;
          resolve();
        }).catch(err => {
          reject(err);
        })
      })
    },
    // 新增一条事件
    handleAddEvent({commit}, formData) {
      return new Promise((resolve, reject) => {
        addEvent(formData).then(res => {
          const data = res.data;
          resolve();
        }).catch(err => {
          reject(err);
        })
      })
    }
  }
}
