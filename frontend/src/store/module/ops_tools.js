import {
	encrypt,
	decrypt,
	randomPassGen,
	addFault
} from '@/api/ops_tools.js'
import { getFaults } from '../../api/ops_tools'

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
    }
	}
}
