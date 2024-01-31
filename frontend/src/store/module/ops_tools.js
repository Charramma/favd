import {
	encrypt,
	decrypt,
	randomPassGen,
	addFault,
  getFaults,
  delFault,
  editFault
} from '@/api/ops_tools.js'

export default {
	state: {
		plain_text: "",
		ciphertext: "",
		random_pass: "",
    faultsInfo: [], // 所有故障信息
    faultCount: "", // 总故障数
    totalPage: "" // 总页数
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
    setTotalPage(state, totalPage) {
      state.totalPage = totalPage
    }
	},
	getters: {
		getCiphertext: state => state.ciphertext,
		getPlaintext: state => state.plain_text,
		getRandompass: state => state.random_pass,
    getFaultCount: state => state.faultCount,
    getTotalPage: state => state.totalPage,
    getFaultsInfo: state => state.faultsInfo
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
    handleEditFault ({commit}, faultinfo) {
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
    handleGetFaults({ commit }, page) {
      return new Promise((resolve, reject) => {
        getFaults({page}).then(res => {
          const data = res.data;
          commit('setFaultsInfo', data.data.faults_info);
          commit('setTotalPage', data.data.total_page);
          commit('setFaultCount', data.data.count);
          resolve();
        }).catch(err => {
          reject(err);
        })
      })
    },
    // 根据fault_id删除故障信息
    handleDelFault({ commit }, fault_id) {
      return new Promise((resolve, reject) => {
        delFault(fault_id).then(res => {
          const data = res.data;
          resolve();
        }).catch(err => {
          reject(err);
        })
      })
    }
	}
}
