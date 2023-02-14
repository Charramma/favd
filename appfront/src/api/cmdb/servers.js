// iview-admin封装好的axios
import axios from '@/libs/api.request'

// 获取server列表
export const getServerList = () => {
  return axios.request({
    url: 'cmdb/servers/',
    method: 'get'
  })
}

// 删除主机
export const delServer = (server_id) => {
  console.log(server_id)
  return axios.request({
    url: 'cmdb/servers/' +server_id + '/',
    method: 'delete'
  })
}