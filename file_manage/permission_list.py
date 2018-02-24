
perm_dict1 = {
    "main_show_index":[
        [
            'index',
        ],
        ['GET',],
        [],
        {},
    ],
    'main_admin_manage':[
        [
            'admin_manage',
            'create_admin_user',
            'update_admin_user',
        ],
        ['GET','POST'],
        [],
        {},
    ],
    "main_show_init_data":[
        [
            'subject',
            'textbook_edition',
            'company',
        ],
        ['GET',],
        [],
        {},
    ],
    "main_change_init_data":[
        [
            'create_subject',
            'update_subject',
            'delete_subject',
            'create_textbook_edition',
            'update_textbook_edition',
            'delete_textbook_edition',
            'create_company',
            'update_company',
            'delete_company',
        ],
        ['POST','GET'],
        [],
        {},
    ],
    "main_show_data_manage":[
        [
            'video',
            'tiku',
            'textbook',
            'album',
        ],
        ['GET',],
        [],
        {},
    ],
    "main_change_data":[
        [
            'create_video',
            'update_video',
            'delete_video',
            'create_tiku',
            'update_tiku',
            'delete_tiku',
            'create_textbook',
            'update_textbook',
            'delete_textbook',
            'create_album',
            'update_album',
            'delete_album',
        ],
        ['POST','GET'],
        [],
        {},
    ],
    "main_show_sys_data":[
        [
            'category_menu',
        ],
        ['GET',],
        [],
        {},
    ],
    "main_change_sys_data":[
        [
            'create_category_menu',
            'update_category_menu',
            'delete_category_menu',
        ],
        ['POST','GET'],
        [],
        {},
    ],
    "main_show_page_view":[
        [
            'daily_pv',
            'daily_active',
            'daily_add',
            'logvisit',
        ],
        ['GET',],
        [],
        {},
    ]
}

permission_list1 = (
    ("show_index",		        "查看首页数据"),
	("show_init_data", 		    "查看初始配置页面"),
	("change_init_data",		"更改初始配置页面"),
	("show_data_manage",	    "查看资源配置"),
	("change_data",		        "更改资源配置"),
	("show_sys_data",		    "查看系统配置"),
	("change_sys_data",		    "更改系统配置"),
	("show_page_view",		    "查看统计数据"),
)
