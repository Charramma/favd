import axios from '@/libs/api.request'

export const encrypt = ({plain_text}) => {
  const data = {
		plain_text
  }
  return axios.request({
    url: 'ops_tools/encrypt',
    data,
    method: 'post'
  })
}

export const decrypt = ({ciphertext}) => {
  const data = {
		ciphertext
  }
  return axios.request({
    url: 'ops_tools/decrypt',
    data,
    method: 'post'
  })
}

export const randomPassGen = ({character, passLength}) => {
	const data = {
		character,
		passLength
	}
	return axios.request({
		url: 'ops_tools/random_pass',
		data,
		method: 'post'
	})
}
/**
* 故障管理
*/
// 新建故障信息
export const addFault = ({faultinfo}) => {
	const data = {
		faultinfo
	}
	return axios.request({
		url: 'ops_tools/faults',
		data,
		method: 'post'
	})
}
// 编辑故障信息
export const editFault = ({fault_id, faultinfo}) => {
	const data = {
		faultinfo
	}
	return axios.request({
		url: `ops_tools/fault/${faultinfo.faultId}`,
		data,
		method: 'put'
	})
}

// 获取所有故障信息
export const getFaults = (page) => {
  return axios.request({
    url: 'ops_tools/faults',
    params: page,
    method: 'get'
  })
}

// 删除故障信息
export const delFault = (fault_id) => {
  return axios.request({
    url: `ops_tools/fault/${fault_id}`,
    method: 'delete'
  })
}

/**
* 事件管理
*/
// 获取所有事件信息
export const getEvents = (page) => {
  return axios.request({
    url: 'ops_tools/events',
    params: page,
    method: 'get'
  })
}
// 删除事件信息
export const delEvent = (event_id) => {
  return axios.request({
    url: `ops_tools/event/${event_id}`,
    method: 'delete'
  })
}
// 新增事件信息
export const addEvent = (data) => {
  return axios.request({
  	url: `ops_tools/events`,
  	data,
  	method: 'post'
  })
}
