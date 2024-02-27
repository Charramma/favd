import axios from '@/libs/api.request'

// 获取所有IDC信息
export const getIdcInfo = ({key, page}) => {
  return axios.request({
    url: 'cmdb/idc',
    params: {key, page},
    method: 'get'
  })
}
// export const getIdcInfo = () => {
//   return axios.request({
//     url: 'cmdb/idc',
//     method: 'get'
//   })
// }

export const delIdcInfo = (idc_id) => {
  return axios.request({
    url: `cmdb/idc/${idc_id}`,
    method: 'delete'
  })
}

export const addIdcInfo = (data) => {
  return axios.request({
    url: 'cmdb/idc',
    data,
    method: 'post'
  })
}

export const updateIdcInfo = (data) => {
  const idc_id = data.idc_id;
  return axios.request({
    url: `cmdb/idc/${idc_id}`,
    data,
    method: 'put'
  })
}
