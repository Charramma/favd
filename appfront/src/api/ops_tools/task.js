import axios from '@/libs/api.request'

export const getTaskList = (page, pagesize, keywords) => {
  return axios.request({
    url: 'ops_tools/tasks/',
    method: 'get',
    params: {
      page, 
      pagesize,
      keywords
    }
  })
}


export const operationTask = (data, meth) => {
  return axios.request({
    url: meth === 'post' ? 'ops_tools/tasks/' : 'ops_tools/tasks/'+data.task_id+'/',
    method: meth,
    data: data
  })
}

export const runTask = (task_id) => {
  return axios.request({
    url: 'ops_tools/run/'+task_id+'/',
    method: 'get',
  })
}


export const getTaskLogList = (page, pagesize, keywords) => {
  return axios.request({
    url: 'ops_tools/tasklogs/',
    method: 'get',
    params: {
      page, 
      pagesize,
      keywords
    }
  })
}