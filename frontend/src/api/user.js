import axios from '@/libs/api.request'

// 登录，接收一个包含userName和password属性的对象作为参数。
export const login = ({ userName, password }) => {
  const data = {
    userName,
    password
  }
	// 向后端的/login接口发送post请求，携带用户名和密码，以完成用户的登录操作
  return axios.request({
    url: 'user/login',
    data,
    method: 'post'
  })
}

// 获取用户信息，主要用于在用户登录后获取其个人信息或其他相关数据。接收一个参数token，以获取与该token相关联的用户信息
export const getUserInfo = (token) => {
  return axios.request({
    url: 'user/',
    params: {
      // token
    },
    method: 'get'
  })
}

// 注册
export const register = ({ userName, email, password }) => {
	const data = {
		userName,
		email,
		password
	}
	return axios.request({
		url: 'user/register',
		data,
		method: 'post'
	})
}

// 注销登录
export const logout = (token) => {
  return axios.request({
    url: 'user/logout',
    method: 'post'
  })
}

export const getUnreadCount = () => {
  return axios.request({
    url: 'message/count',
    method: 'get'
  })
}

export const getMessage = () => {
  return axios.request({
    url: 'message/init',
    method: 'get'
  })
}

export const getContentByMsgId = msg_id => {
  return axios.request({
    url: 'message/content',
    method: 'get',
    params: {
      msg_id
    }
  })
}

export const hasRead = msg_id => {
  return axios.request({
    url: 'message/has_read',
    method: 'post',
    data: {
      msg_id
    }
  })
}

export const removeReaded = msg_id => {
  return axios.request({
    url: 'message/remove_readed',
    method: 'post',
    data: {
      msg_id
    }
  })
}

export const restoreTrash = msg_id => {
  return axios.request({
    url: 'message/restore',
    method: 'post',
    data: {
      msg_id
    }
  })
}
