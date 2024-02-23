import axios from '@/libs/api.request'

// 获取所有IDC信息
export const getIdcInfo = (page) => {
  return axios.request({
    url: 'cmdb/idc',
    params: page,
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
