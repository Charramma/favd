import axios from '@/libs/api.request'

export const login = ({ userName, password }) => {
  const data = {
    userName,
    password
  }
  return axios.request({
    url: 'user/login/',
    data,
    method: 'post'
  })
}

export const getUserInfo = (token) => {
  return axios.request({

    url: 'user/',
    params: {
      // token
    },
    method: 'get'
  })
}

export const logout = (token) => {
  return axios.request({
    url: 'logout',
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
import Main from '@/components/main'
import parentView from '@/components/parent-view'

/**
 * iview-admin中meta除了原生参数外可配置的参数:
 * meta: {
 *  title: { String|Number|Function }
 *         显示在侧边栏、面包屑和标签栏的文字
 *         使用'{{ 多语言字段 }}'形式结合多语言使用，例子看多语言的路由配置;
 *         可以传入一个回调函数，参数是当前路由对象，例子看动态路由和带参路由
 *  hideInBread: (false) 设为true后此级路由将不会出现在面包屑中，示例看QQ群路由配置
 *  hideInMenu: (false) 设为true后在左侧菜单不会显示该页面选项
 *  notCache: (false) 设为true后页面在切换标签后不会缓存，如果需要缓存，无需设置这个字段，而且需要设置页面组件name属性和路由配置的name一致
 *  access: (null) 可访问该页面的权限数组，当前路由设置的权限会影响子路由
 *  icon: (-) 该页面在左侧菜单、面包屑和标签导航处显示的图标，如果是自定义图标，需要在图标名称前加下划线'_'
 *  beforeCloseName: (-) 设置该字段，则在关闭当前tab页时会去'@/router/before-close.js'里寻找该字段名对应的方法，作为关闭前的钩子函数
 * }
 */

export default [
  // 登录
  {
    path: '/login',
    name: 'login',
    meta: {
      title: 'Login - 登录',
      hideInMenu: true
    },
    component: () => import('@/view/login/login.vue')
  },
  // 首页
  {
    path: '/',
    name: '_home',
    redirect: '/home',
    component: Main,
    meta: {
      hideInMenu: true,
      notCache: true
    },
    children: [{
      path: '/home',
      name: 'home',
      meta: {
        hideInMenu: true,
        title: '首页',
        notCache: true,
        icon: 'md-home'
      },
      component: () => import('@/view/single-page/home')
    }]
  },
  // 订单中心
  {
    path: '/order',
    name: 'order',
    meta: {
      title: '工单管理',
      icon: 'ios-menu'
    },
    component: Main,
    children: [{
        path: 'taskOrderList',
        name: 'taskOrderList',
        meta: {
          icon: 'md-list',
          title: '工单列表'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'historyTaskList',
        name: 'historyTaskList',
        meta: {
          icon: 'md-checkbox-outline',
          title: '历史工单'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      }
    ]
  },
  // 资源申购
  {
    path: '/assetPurchase',
    name: 'assetPurchase',
    meta: {
      title: '资源申购',
      icon: 'logo-usd'
    },
    component: Main,
    children: [{
        path: 'assetPurchaseAWS',
        name: 'assetPurchaseAWS',
        meta: {
          icon: 'md-cloudy',
          title: '资源申购-亚马逊'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'assetPurchaseALi',
        name: 'assetPurchaseALi',
        meta: {
          icon: 'md-cloudy',
          title: '资源申购-阿里云'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'assetPurchaseQcloud',
        name: 'assetPurchaseQcloud',
        meta: {
          icon: 'md-cloudy',
          title: '资源申购-腾讯云'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      }
    ]
  },
  // 资产管理
  {
    path: '/cmdb',
    name: 'cmdb',
    meta: {
      title: '资产管理',
      icon: 'md-cube'
    },
    component: Main,
    children: [{
        path: 'asset_server',
        name: 'asset_server',
        meta: {
          icon: 'md-cube',
          title: '主机管理'
        },
        component: () => import('@/view/cmdb/asset-servers.vue')
      },
      {
        path: 'asset_db',
        name: 'asset_db',
        meta: {
          icon: 'logo-buffer',
          title: 'DB管理'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'asset_idc',
        name: 'asset_idc',
        meta: {
          icon: 'ios-albums',
          title: 'IDC管理'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'operational_audit',
        name: 'operational_audit',
        meta: {
          icon: 'ios-podium',
          title: '操作审计'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'tag_mg',
        name: 'tag_mg',
        meta: {
          icon: 'ios-pricetags',
          title: '标签管理'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'user_mg',
        name: 'user_mg',
        meta: {
          icon: 'ios-people',
          title: '管理用户'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'asset_config',
        name: 'asset_config',
        meta: {
          icon: 'ios-hammer',
          title: '资产配置'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      }
    ]
  },
  // 作业配置
  {
    path: '/operation_center',
    name: 'operation_center',
    meta: {
      title: '作业配置',
      icon: 'ios-briefcase'
    },
    component: Main,
    children: [{
        path: 'publishConfig',
        name: 'publishConfig',
        meta: {
          icon: 'md-options',
          title: '应用配置'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'codeRepository',
        name: 'codeRepository',
        meta: {
          icon: 'logo-github',
          title: '代码仓库'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'dockerRegistry',
        name: 'dockerRegistry',
        meta: {
          icon: 'md-apps',
          title: '镜像仓库'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'task_layout',
        name: 'task_layout',
        meta: {
          access: ['super_admin'],
          icon: 'md-bulb',
          // showAlways: true,
          title: '任务模板'
        },
        component: parentView,
        children: [{
            path: 'commandlist',
            name: 'commandlist',
            meta: {
              icon: 'ios-cafe-outline',
              title: '命令管理'
            },
            component: () => import('@/view/components/asset-server/asset-server.vue')
          },
          {
            path: 'templist',
            name: 'templist',
            meta: {
              icon: 'ios-list',
              title: '模板管理'
            },
            component: () => import('@/view/components/asset-server/asset-server.vue')
          },
          {
            path: 'argslist',
            name: 'argslist',
            meta: {
              icon: 'ios-code',
              title: '参数管理'
            },
            component: () => import('@/view/components/asset-server/asset-server.vue')
          },
          {
            path: 'taskuser',
            name: 'taskuser',
            meta: {
              icon: 'ios-person-add',
              title: '执行用户'
            },
            component: () => import('@/view/components/asset-server/asset-server.vue')
          }
        ]
      }
    ]
  },
  // 定时任务
  {
    path: '/cron',
    name: 'cron',
    meta: {
      title: '定时任务',
      icon: 'md-time'
    },
    component: Main,
    children: [{
        path: 'cronjobs',
        name: 'cronjobs',
        meta: {
          icon: 'md-list',
          title: '定时列表'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'cronlogs',
        name: 'cronlogs',
        meta: {
          icon: 'ios-paper',
          title: '任务日志'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      }
    ]
  },
  // 配置中心
  {
    path: '/confd',
    name: 'confd',
    component: Main,
    meta: {
      hideInBread: true
    },
    children: [{
      path: 'confd_project',
      name: 'confd_project',
      meta: {
        icon: 'ios-construct',
        title: '配置中心'
      },
      component: () => import('@/view/components/asset-server/asset-server.vue')
    }]
  },
  // 域名管理
  {
    path: '/domain',
    name: 'domain',
    meta: {
      title: '域名管理',
      icon: 'md-barcode'
    },
    component: Main,
    children: [{
        path: 'domain_name_manage',
        name: 'domain_name_manage',
        meta: {
          icon: 'md-barcode',
          title: 'BIND解析'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'domain_name_monitor',
        name: 'domain_name_monitor',
        meta: {
          icon: 'md-barcode',
          title: '域名监控'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      }
    ]
  },
  // 运维工具
  {
    path: '/devopstools',
    name: 'devopstools',
    meta: {
      icon: 'md-hammer',
      title: '运维工具'
    },
    component: Main,
    children: [{
        path: 'remind_manager',
        name: 'remind_manager',
        meta: {
          title: '提醒管理',
          icon: 'md-notifications'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'project_manager',
        name: 'project_manager',
        meta: {
          title: '项目管理',
          icon: 'md-clipboard'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'event_manager',
        name: 'event_manager',
        meta: {
          title: '事件管理',
          icon: 'ios-paper-outline'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'fault_manager',
        name: 'fault_manager',
        meta: {
          title: '故障管理',
          icon: 'ios-paper-outline'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'password_mycrypy',
        name: 'password_mycrypy',
        meta: {
          title: '加密解密',
          icon: 'ios-key'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      }
    ]
  },
  // 监控报警
  {
    path: '/monitoringalarm',
    name: 'monitoringalarm',
    component: Main,
    meta: {
      title: '监控报警',
      icon: 'ios-notifications'
    },
    children: [{
        path: 'zabbix_manager',
        name: 'zabbix_manager',
        meta: {
          title: 'ZABBIX',
          icon: 'ios-stats-outline'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'prometheus_alert',
        name: 'prometheus_alert',
        meta: {
          title: 'Prometheus',
          icon: 'ios-stats'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      }
    ]
  },
  // 用户管理
  {
    path: '/usermanage',
    name: 'usermanage',
    component: Main,
    meta: {
      title: '用户管理',
      icon: 'ios-contact'
    },
    children: [{
        path: 'user',
        name: 'user',
        meta: {
          title: '用户列表',
          icon: 'ios-people-outline'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'functions',
        name: 'functions',
        meta: {
          title: '权限列表',
          icon: 'ios-stats'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'menus',
        name: 'menus',
        meta: {
          title: '菜单组件',
          icon: 'ios-menu'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'role',
        name: 'role',
        meta: {
          title: '角色管理',
          icon: 'ios-people-outline'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      }
    ]
  },
  // 系统管理
  {
    path: '/systemmanage',
    name: 'systemmanage',
    component: Main,
    meta: {
      title: '系统管理',
      icon: 'md-settings'
    },
    children: [{
        path: 'system',
        name: 'system',
        meta: {
          title: '系统配置',
          icon: 'ios-options'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'resourceManagement',
        name: 'resourceManagement',
        meta: {
          title: '资源管理',
          icon: 'ios-pie'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      },
      {
        path: 'systemlog',
        name: 'systemlog',
        meta: {
          title: '系统日志',
          icon: 'ios-paper'
        },
        component: () => import('@/view/components/asset-server/asset-server.vue')
      }
    ]
  },
  // 401
  {
    path: '/401',
    name: 'error_401',
    meta: {
      hideInMenu: true
    },
    component: () => import('@/view/error-page/401.vue')
  },
  // 500
  {
    path: '/500',
    name: 'error_500',
    meta: {
      hideInMenu: true
    },
    component: () => import('@/view/error-page/500.vue')
  },
  // 404
  {
    path: '*',
    name: 'error_404',
    meta: {
      hideInMenu: true
    },
    component: () => import('@/view/error-page/404.vue')
  }
]
