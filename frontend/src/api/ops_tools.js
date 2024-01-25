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

// 获取故障信息
export const getFaults = (page) => {
  const data = {
    page
  }
  return axios.request({
    url: 'ops_tools/faults',
    data,
    method: 'get'
  })
}
