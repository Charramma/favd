import {
	login,
	logout,
	getUserInfo,
	register,
	getMessage,
	getContentByMsgId,
	hasRead,
	removeReaded,
	restoreTrash,
	getUnreadCount
} from '@/api/user'
import {
	setToken,
	getToken
} from '@/libs/util'

export default {
	state: {
		userName: '',
		userId: '',
		avatarImgPath: '',
		token: getToken(),
		access: '',
		hasGetInfo: false,
		unreadCount: 0,
		messageUnreadList: [],
		messageReadedList: [],
		messageTrashList: [],
		messageContentStore: {}
	},
	mutations: {
		setAvatar(state, avatarPath) {
			state.avatarImgPath = avatarPath
		},
		setUserId(state, id) {
			state.userId = id
		},
		setUserName(state, name) {
			state.userName = name
		},
		setAccess(state, access) {
			state.access = access
		},
		setToken(state, token) {
			state.token = token
			setToken(token)
		},
		setHasGetInfo(state, status) {
			state.hasGetInfo = status
		},
		setMessageCount(state, count) {
			state.unreadCount = count
		},
		setMessageUnreadList(state, list) {
			state.messageUnreadList = list
		},
		setMessageReadedList(state, list) {
			state.messageReadedList = list
		},
		setMessageTrashList(state, list) {
			state.messageTrashList = list
		},
		updateMessageContentStore(state, {
			msg_id,
			content
		}) {
			state.messageContentStore[msg_id] = content
		},
		moveMsg(state, {
			from,
			to,
			msg_id
		}) {
			const index = state[from].findIndex(_ => _.msg_id === msg_id)
			const msgItem = state[from].splice(index, 1)[0]
			msgItem.loading = false
			state[to].unshift(msgItem)
		}
	},
	getters: {
		messageUnreadCount: state => state.messageUnreadList.length,
		messageReadedCount: state => state.messageReadedList.length,
		messageTrashCount: state => state.messageTrashList.length
	},
	actions: {
		// 登录
		handleLogin({
			commit
		}, {
			userName,
			password
		}) {
			userName = userName.trim() // 去掉首尾空格
			// 返回一个Promise对象
			return new Promise((resolve, reject) => {
				// 调用login函数，传递修建过后的的用户名和密码
				login({
					userName,
					password
				}).then(res => {
					// 当 login 函数成功返回后，将从响应中获取的 token 提交给 Vuex store 中的 setToken mutation，并最终 resolve Promise
					const data = res.data
					commit('setToken', data.data.token)
					resolve()
				}).catch(err => {
					// 请求返回了401错误
					if (err.response && err.response.status === 401) {
						reject('用户名或密码输入错误！')
					} else {
						reject(err)
					}
				})
			})
		},
		// 注册
		handleRegister({
			commit
		}, {
			userName,
			email,
			password
		}) {
			userName = userName.trim();
			email = email.trim();
			return new Promise((resolve, reject) => {
				register({
					userName,
					email,
					password
				}).then(res => {
					const data = res.data;
					resolve();
				}).catch(err => {
					reject(err)
				})
			})
		},
		// 退出登录
		handleLogOut({
			state,
			commit
		}) {
			return new Promise((resolve, reject) => {
				// logout(state.token).then(() => {
				//   commit('setToken', '')
				//   commit('setAccess', [])
				//   resolve()
				// }).catch(err => {
				//   reject(err)
				// })

				// 如果你的退出登录无需请求接口，则可以直接使用下面三行代码而无需使用logout调用接口
				commit('setToken', '')
				commit('setAccess', [])
				resolve()
			})
		},
		// 获取用户相关信息
		getUserInfo({
			state,
			commit
		}) {
			return new Promise((resolve, reject) => {
				try {
					// 调用名为 getUserInfo 的函数（定义在src/api/user.js中），并传递当前用户的 token
					getUserInfo(state.token).then(res => {
						const data = res.data
						commit('setAvatar', 'https://i.loli.net/2017/08/21/599a521472424.jpg')	// 头像
						commit('setUserName', data.data.user_profile_name) // 用户名
						commit('setUserId', data.data.user_profile_id) // 用户id 
						// commit('setAccess', data.access)  // 用户角色
						commit('setHasGetInfo', true) // 表示已经成功获取到用户信息
						resolve(data)
					}).catch(err => {
						reject(err)
					})
				} catch (error) {
					reject(error)
				}
			})
		},
		// 此方法用来获取未读消息条数，接口只返回数值，不返回消息列表
		getUnreadMessageCount({
			state,
			commit
		}) {
			getUnreadCount().then(res => {
				const {
					data
				} = res
				commit('setMessageCount', data)
			})
		},
		// 获取消息列表，其中包含未读、已读、回收站三个列表
		getMessageList({
			state,
			commit
		}) {
			return new Promise((resolve, reject) => {
				getMessage().then(res => {
					const {
						unread,
						readed,
						trash
					} = res.data
					commit('setMessageUnreadList', unread.sort((a, b) => new Date(b.create_time) - new Date(a
						.create_time)))
					commit('setMessageReadedList', readed.map(_ => {
						_.loading = false
						return _
					}).sort((a, b) => new Date(b.create_time) - new Date(a.create_time)))
					commit('setMessageTrashList', trash.map(_ => {
						_.loading = false
						return _
					}).sort((a, b) => new Date(b.create_time) - new Date(a.create_time)))
					resolve()
				}).catch(error => {
					reject(error)
				})
			})
		},
		// 根据当前点击的消息的id获取内容
		getContentByMsgId({
			state,
			commit
		}, {
			msg_id
		}) {
			return new Promise((resolve, reject) => {
				let contentItem = state.messageContentStore[msg_id]
				if (contentItem) {
					resolve(contentItem)
				} else {
					getContentByMsgId(msg_id).then(res => {
						const content = res.data
						commit('updateMessageContentStore', {
							msg_id,
							content
						})
						resolve(content)
					})
				}
			})
		},
		// 把一个未读消息标记为已读
		hasRead({
			state,
			commit
		}, {
			msg_id
		}) {
			return new Promise((resolve, reject) => {
				hasRead(msg_id).then(() => {
					commit('moveMsg', {
						from: 'messageUnreadList',
						to: 'messageReadedList',
						msg_id
					})
					commit('setMessageCount', state.unreadCount - 1)
					resolve()
				}).catch(error => {
					reject(error)
				})
			})
		},
		// 删除一个已读消息到回收站
		removeReaded({
			commit
		}, {
			msg_id
		}) {
			return new Promise((resolve, reject) => {
				removeReaded(msg_id).then(() => {
					commit('moveMsg', {
						from: 'messageReadedList',
						to: 'messageTrashList',
						msg_id
					})
					resolve()
				}).catch(error => {
					reject(error)
				})
			})
		},
		// 还原一个已删除消息到已读消息
		restoreTrash({
			commit
		}, {
			msg_id
		}) {
			return new Promise((resolve, reject) => {
				restoreTrash(msg_id).then(() => {
					commit('moveMsg', {
						from: 'messageTrashList',
						to: 'messageReadedList',
						msg_id
					})
					resolve()
				}).catch(error => {
					reject(error)
				})
			})
		}
	}
}