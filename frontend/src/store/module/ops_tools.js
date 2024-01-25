import {
	encrypt,
	decrypt,
	randomPassGen,
	addFault
} from '@/api/ops_tools.js'

export default {
	state: {
		plain_text: "",
		ciphertext: "",
		random_pass: ""
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
		}
	},
	getters: {
		getCiphertext: state => state.ciphertext,
		getPlaintext: state => state.plain_text,
		getRandompass: state => state.random_pass
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
		}
	}
}