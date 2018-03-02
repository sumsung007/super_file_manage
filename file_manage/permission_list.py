perm_dict = {
    "user_manage":[
        [
            'user_manage',
        ],
        ['GET', ],
        [],
        {},
    ],
    "create_user":[
        [
            'create_user',
        ],
        ['POST',],
        [],
        {},
    ],
    "update_user":[
        [
            'update_user',
        ],
        ['GET', 'POST',],
        [],
        {},
    ],
    "delete_user":[
        [
            'delete_user',
        ],
        ['POST',],
        [],
        {},
    ],
    "change_password":[
        [
            'change_password',
        ],
        ['POST',],
        [],
        {},
    ],
    "file_manage_show_index":[
        [
            'index',
            'request_file_tree',
            'request_file_list',
        ],
        ['GET',],
        [],
        {},
    ],
    'file_manage_create_dir':[
        [
            'create_dir',
        ],
        ['POST',],
        [],
        {},
    ],
    "file_manage_rename_dir":[
        [
            'rename_dir',
        ],
        ['POST', ],
        [],
        {},
    ],
    "file_manage_delete_dir":[
        [
            'delete_dir',
        ],
        ['POST', ],
        [],
        {},
    ],
    "file_manage_add_files":[
        [
            'add_files',
        ],
        ['POST', ],
        [],
        {},
    ],
    "file_manage_mv_dir":[
        [
            'mv_dir',
        ],
        ['POST', ],
        [],
        {},
    ],
}

permission_list = (
    ("show_index", "查看首页数据"),
    ("create_dir", "可以创建文件夹"),
    ("rename_dir", "可以更改文件名"),
    ("delete_dir", "可以删除文件"),
    ("add_files", "可以上传文件"),
    ("mv_dir", "可以移动文件"),
)
