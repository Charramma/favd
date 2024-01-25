import Main from '@/components/main'
import parentView from '@/components/parent-view'
// import {
// 	component
// } from 'vue/types/umd'

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

export default [{
		path: '/login',
		name: 'login',
		meta: {
			title: 'Login - 登录',
			hideInMenu: true
		},
		component: () => import('@/view/login/login.vue')
	},
	{
		path: '/register',
		name: 'register',
		meta: {
			title: 'Register - 注册',
			hideInMenu: true
		},
		component: () => import('@/view/register/register.vue')
	},
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
	// 工单管理
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
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'historyTaskList',
        name: 'historyTaskList',
        meta: {
          icon: 'md-checkbox-outline',
          title: '历史工单'
        },
        component: () => import('@/view/newrouter/lalala.vue')
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
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'assetPurchaseALi',
        name: 'assetPurchaseALi',
        meta: {
          icon: 'md-cloudy',
          title: '资源申购-阿里云'
        },
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'assetPurchaseQcloud',
        name: 'assetPurchaseQcloud',
        meta: {
          icon: 'md-cloudy',
          title: '资源申购-腾讯云'
        },
        component: () => import('@/view/newrouter/lalala.vue')
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
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'asset_db',
        name: 'asset_db',
        meta: {
          icon: 'logo-buffer',
          title: 'DB管理'
        },
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'asset_idc',
        name: 'asset_idc',
        meta: {
          icon: 'ios-albums',
          title: 'IDC管理'
        },
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'operational_audit',
        name: 'operational_audit',
        meta: {
          icon: 'ios-podium',
          title: '操作审计'
        },
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'tag_mg',
        name: 'tag_mg',
        meta: {
          icon: 'ios-pricetags',
          title: '标签管理'
        },
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'user_mg',
        name: 'user_mg',
        meta: {
          icon: 'ios-people',
          title: '管理用户'
        },
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'asset_config',
        name: 'asset_config',
        meta: {
          icon: 'ios-hammer',
          title: '资产配置'
        },
        component: () => import('@/view/newrouter/lalala.vue')
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
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'codeRepository',
        name: 'codeRepository',
        meta: {
          icon: 'logo-github',
          title: '代码仓库'
        },
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'dockerRegistry',
        name: 'dockerRegistry',
        meta: {
          icon: 'md-apps',
          title: '镜像仓库'
        },
        component: () => import('@/view/newrouter/lalala.vue')
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
            component: () => import('@/view/newrouter/lalala.vue')
          },
          {
            path: 'templist',
            name: 'templist',
            meta: {
              icon: 'ios-list',
              title: '模板管理'
            },
            component: () => import('@/view/newrouter/lalala.vue')
          },
          {
            path: 'argslist',
            name: 'argslist',
            meta: {
              icon: 'ios-code',
              title: '参数管理'
            },
            component: () => import('@/view/newrouter/lalala.vue')
          },
          {
            path: 'taskuser',
            name: 'taskuser',
            meta: {
              icon: 'ios-person-add',
              title: '执行用户'
            },
            component: () => import('@/view/newrouter/lalala.vue')
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
          title: '任务列表'
        },
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'cronlogs',
        name: 'cronlogs',
        meta: {
          icon: 'ios-paper',
          title: '任务日志'
        },
        component: () => import('@/view/newrouter/lalala.vue')
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
      component: () => import('@/view/newrouter/lalala.vue')
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
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'domain_name_monitor',
        name: 'domain_name_monitor',
        meta: {
          icon: 'md-barcode',
          title: '域名监控'
        },
        component: () => import('@/view/newrouter/lalala.vue')
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
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'project_manager',
        name: 'project_manager',
        meta: {
          title: '项目管理',
          icon: 'md-clipboard'
        },
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'event_manager',
        name: 'event_manager',
        meta: {
          title: '事件管理',
          icon: 'ios-paper-outline'
        },
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'fault_manager',
        name: 'fault_manager',
        meta: {
          title: '故障管理',
          icon: 'ios-paper-outline'
        },
        component: () => import('@/view/ops_tools/faults_manage.vue')
      },
      {
        path: 'password_mycrypy',
        name: 'password_mycrypy',
        meta: {
          title: '加密解密',
          icon: 'ios-key'
        },
        component: () => import('@/view/ops_tools/secret_code.vue')
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
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'prometheus_alert',
        name: 'prometheus_alert',
        meta: {
          title: 'Prometheus',
          icon: 'ios-stats'
        },
        component: () => import('@/view/newrouter/lalala.vue')
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
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'functions',
        name: 'functions',
        meta: {
          title: '权限列表',
          icon: 'ios-stats'
        },
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'menus',
        name: 'menus',
        meta: {
          title: '菜单组件',
          icon: 'ios-menu'
        },
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'role',
        name: 'role',
        meta: {
          title: '角色管理',
          icon: 'ios-people-outline'
        },
        component: () => import('@/view/newrouter/lalala.vue')
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
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'resourceManagement',
        name: 'resourceManagement',
        meta: {
          title: '资源管理',
          icon: 'ios-pie'
        },
        component: () => import('@/view/newrouter/lalala.vue')
      },
      {
        path: 'systemlog',
        name: 'systemlog',
        meta: {
          title: '系统日志',
          icon: 'ios-paper'
        },
        component: () => import('@/view/newrouter/lalala.vue')
      }
    ]
  },
	{
	  path: '/tools_methods',
	  name: 'tools_methods',
	  meta: {
	    hideInBread: true
	  },
	  component: Main,
	  children: [
	    {
	      path: 'tools_methods_page',
	      name: 'tools_methods_page',
	      meta: {
	        icon: 'ios-hammer',
	        title: '工具方法',
	        beforeCloseName: 'before_close_normal'
	      },
	      component: () => import('@/view/tools-methods/tools-methods.vue')
	    }
	  ]
	},
	{
		path: '/join',
		name: 'join',
		component: Main,
		meta: {
			hideInBread: true
		},
		children: [{
			path: 'join_page',
			name: 'join_page',
			meta: {
				icon: '_qq',
				title: 'QQ群'
			},
			component: () => import('@/view/join-page.vue')
		}]
	},
	{
		path: '/message',
		name: 'message',
		component: Main,
		meta: {
			hideInBread: true,
			hideInMenu: true
		},
		children: [{
			path: 'message_page',
			name: 'message_page',
			meta: {
				icon: 'md-notifications',
				title: '消息中心'
			},
			component: () => import('@/view/single-page/message/index.vue')
		}]
	},
	{
		path: '/components',
		name: 'components',
		meta: {
			icon: 'logo-buffer',
			title: '组件'
		},
		component: Main,
		children: [{
				path: 'tree_select_page',
				name: 'tree_select_page',
				meta: {
					icon: 'md-arrow-dropdown-circle',
					title: '树状下拉选择器'
				},
				component: () => import('@/view/components/tree-select/index.vue')
			},
			{
				path: 'count_to_page',
				name: 'count_to_page',
				meta: {
					icon: 'md-trending-up',
					title: '数字渐变'
				},
				component: () => import('@/view/components/count-to/count-to.vue')
			},
			{
				path: 'drag_list_page',
				name: 'drag_list_page',
				meta: {
					icon: 'ios-infinite',
					title: '拖拽列表'
				},
				component: () => import('@/view/components/drag-list/drag-list.vue')
			},
			{
				path: 'drag_drawer_page',
				name: 'drag_drawer_page',
				meta: {
					icon: 'md-list',
					title: '可拖拽抽屉'
				},
				component: () => import('@/view/components/drag-drawer')
			},
			{
				path: 'org_tree_page',
				name: 'org_tree_page',
				meta: {
					icon: 'ios-people',
					title: '组织结构树'
				},
				component: () => import('@/view/components/org-tree')
			},
			{
				path: 'tree_table_page',
				name: 'tree_table_page',
				meta: {
					icon: 'md-git-branch',
					title: '树状表格'
				},
				component: () => import('@/view/components/tree-table/index.vue')
			},
			{
				path: 'cropper_page',
				name: 'cropper_page',
				meta: {
					icon: 'md-crop',
					title: '图片裁剪'
				},
				component: () => import('@/view/components/cropper/cropper.vue')
			},
			{
				path: 'tables_page',
				name: 'tables_page',
				meta: {
					icon: 'md-grid',
					title: '多功能表格'
				},
				component: () => import('@/view/components/tables/tables.vue')
			},
			{
				path: 'split_pane_page',
				name: 'split_pane_page',
				meta: {
					icon: 'md-pause',
					title: '分割窗口'
				},
				component: () => import('@/view/components/split-pane/split-pane.vue')
			},
			{
				path: 'markdown_page',
				name: 'markdown_page',
				meta: {
					icon: 'logo-markdown',
					title: 'Markdown编辑器'
				},
				component: () => import('@/view/components/markdown/markdown.vue')
			},
			{
				path: 'editor_page',
				name: 'editor_page',
				meta: {
					icon: 'ios-create',
					title: '富文本编辑器'
				},
				component: () => import('@/view/components/editor/editor.vue')
			},
			{
				path: 'icons_page',
				name: 'icons_page',
				meta: {
					icon: '_bear',
					title: '自定义图标'
				},
				component: () => import('@/view/components/icons/icons.vue')
			}
		]
	},
	{
		path: '/update',
		name: 'update',
		meta: {
			icon: 'md-cloud-upload',
			title: '数据上传'
		},
		component: Main,
		children: [{
				path: 'update_table_page',
				name: 'update_table_page',
				meta: {
					icon: 'ios-document',
					title: '上传Csv'
				},
				component: () => import('@/view/update/update-table.vue')
			},
			{
				path: 'update_paste_page',
				name: 'update_paste_page',
				meta: {
					icon: 'md-clipboard',
					title: '粘贴表格数据'
				},
				component: () => import('@/view/update/update-paste.vue')
			}
		]
	},
	{
		path: '/excel',
		name: 'excel',
		meta: {
			icon: 'ios-stats',
			title: 'EXCEL导入导出'
		},
		component: Main,
		children: [{
				path: 'upload-excel',
				name: 'upload-excel',
				meta: {
					icon: 'md-add',
					title: '导入EXCEL'
				},
				component: () => import('@/view/excel/upload-excel.vue')
			},
			{
				path: 'export-excel',
				name: 'export-excel',
				meta: {
					icon: 'md-download',
					title: '导出EXCEL'
				},
				component: () => import('@/view/excel/export-excel.vue')
			}
		]
	},
	{
		path: '/tools_methods',
		name: 'tools_methods',
		meta: {
			hideInBread: true
		},
		component: Main,
		children: [{
			path: 'tools_methods_page',
			name: 'tools_methods_page',
			meta: {
				icon: 'ios-hammer',
				title: '工具方法',
				beforeCloseName: 'before_close_normal'
			},
			component: () => import('@/view/tools-methods/tools-methods.vue')
		}]
	},
	{
		path: '/i18n',
		name: 'i18n',
		meta: {
			hideInBread: true
		},
		component: Main,
		children: [{
			path: 'i18n_page',
			name: 'i18n_page',
			meta: {
				icon: 'md-planet',
				title: 'i18n - {{ i18n_page }}'
			},
			component: () => import('@/view/i18n/i18n-page.vue')
		}]
	},
	{
		path: '/error_store',
		name: 'error_store',
		meta: {
			hideInBread: true
		},
		component: Main,
		children: [{
			path: 'error_store_page',
			name: 'error_store_page',
			meta: {
				icon: 'ios-bug',
				title: '错误收集'
			},
			component: () => import('@/view/error-store/error-store.vue')
		}]
	},
	{
		path: '/error_logger',
		name: 'error_logger',
		meta: {
			hideInBread: true,
			hideInMenu: true
		},
		component: Main,
		children: [{
			path: 'error_logger_page',
			name: 'error_logger_page',
			meta: {
				icon: 'ios-bug',
				title: '错误收集'
			},
			component: () => import('@/view/single-page/error-logger.vue')
		}]
	},
	{
		path: '/directive',
		name: 'directive',
		meta: {
			hideInBread: true
		},
		component: Main,
		children: [{
			path: 'directive_page',
			name: 'directive_page',
			meta: {
				icon: 'ios-navigate',
				title: '指令'
			},
			component: () => import('@/view/directive/directive.vue')
		}]
	},
	{
		path: '/multilevel',
		name: 'multilevel',
		meta: {
			icon: 'md-menu',
			title: '多级菜单'
		},
		component: Main,
		children: [{
				path: 'level_2_1',
				name: 'level_2_1',
				meta: {
					icon: 'md-funnel',
					title: '二级-1'
				},
				component: () => import('@/view/multilevel/level-2-1.vue')
			},
			{
				path: 'level_2_2',
				name: 'level_2_2',
				meta: {
					access: ['super_admin'],
					icon: 'md-funnel',
					showAlways: true,
					title: '二级-2'
				},
				component: parentView,
				children: [{
						path: 'level_2_2_1',
						name: 'level_2_2_1',
						meta: {
							icon: 'md-funnel',
							title: '三级'
						},
						component: () => import('@/view/multilevel/level-2-2/level-2-2-1.vue')
					},
					{
						path: 'level_2_2_2',
						name: 'level_2_2_2',
						meta: {
							icon: 'md-funnel',
							title: '三级'
						},
						component: () => import('@/view/multilevel/level-2-2/level-2-2-2.vue')
					}
				]
			},
			{
				path: 'level_2_3',
				name: 'level_2_3',
				meta: {
					icon: 'md-funnel',
					title: '二级-3'
				},
				component: () => import('@/view/multilevel/level-2-3.vue')
			}
		]
	},
	{
		path: '/argu',
		name: 'argu',
		meta: {
			hideInMenu: true
		},
		component: Main,
		children: [{
				path: 'params/:id',
				name: 'params',
				meta: {
					icon: 'md-flower',
					title: route => `{{ params }}-${route.params.id}`,
					notCache: true,
					beforeCloseName: 'before_close_normal'
				},
				component: () => import('@/view/argu-page/params.vue')
			},
			{
				path: 'query',
				name: 'query',
				meta: {
					icon: 'md-flower',
					title: route => `{{ query }}-${route.query.id}`,
					notCache: true
				},
				component: () => import('@/view/argu-page/query.vue')
			}
		]
	},
	{
		path: '/401',
		name: 'error_401',
		meta: {
			hideInMenu: true
		},
		component: () => import('@/view/error-page/401.vue')
	},
	{
		path: '/500',
		name: 'error_500',
		meta: {
			hideInMenu: true
		},
		component: () => import('@/view/error-page/500.vue')
	},
	{
		path: '*',
		name: 'error_404',
		meta: {
			hideInMenu: true
		},
		component: () => import('@/view/error-page/404.vue')
	}
]