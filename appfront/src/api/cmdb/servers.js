// iview-admin封装好的axios
import axios from '@/libs/api.request'

export const getServerList = () => {
  return axios.request({
    url: 'cmdb/servers/',
    method: 'get'
  })
}

export const delServer = (server_id) => {
  console.log(server_id)
  return axios.request({
    url: 'cmdb/servers/' +server_id + '/',
    method: 'delete'
  })
}