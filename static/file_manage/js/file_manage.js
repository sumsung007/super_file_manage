$(function (){
    $('#page2').addClass('active')
    $('#jstree').jstree({ 
        "plugins" : ['contextmenu','unique','state'],
        'contextmenu':{
            'items':{
                "ccp":null,
                "create" : {
					"separator_before"	: false,
					"separator_after"	: true,
					"_disabled"			: false, //(this.check("create_node", data.reference, {}, "last")),
					"label"				: "Create",
					"action"			: function (data) {
						var inst = $.jstree.reference(data.reference),
							obj = inst.get_node(data.reference);
						inst.create_node(obj, {}, "last", function (new_node) {
							try {
								inst.edit(new_node);
							} catch (ex) {
								setTimeout(function () { inst.edit(new_node); },0);
							}
						});
					}
				},
				"rename" : {
					"separator_before"	: false,
					"separator_after"	: false,
					"_disabled"			: false, //(this.check("rename_node", data.reference, this.get_parent(data.reference), "")),
					"label"				: "Rename",
					/*!
					"shortcut"			: 113,
					"shortcut_label"	: 'F2',
					"icon"				: "glyphicon glyphicon-leaf",
					*/
					"action"			: function (data) {
						var inst = $.jstree.reference(data.reference),
							obj = inst.get_node(data.reference);
						inst.edit(obj);
					}
				},
				"remove" : {
					"separator_before"	: false,
					"icon"				: false,
					"separator_after"	: false,
					"_disabled"			: false, //(this.check("delete_node", data.reference, this.get_parent(data.reference), "")),
					"label"				: "Delete",
					"action"			: function (data) {
						var inst = $.jstree.reference(data.reference),
							obj = inst.get_node(data.reference);
						if(inst.is_selected(obj)) {
							inst.delete_node(inst.get_selected());
						}
						else {
							inst.delete_node(obj);
						}
					}
				},
            }
        },
        'core' : {
            'data' : {
                "url" : "/file_manage/api/request_file_tree?lazy",
                "data" : function (node) {
                    var parents = $('#jstree').jstree(true).get_path(node)
                    var file_path = '#/';
                    for(var i=0;i<parents.length-1;i++){
                        file_path += parents[i] + '/';
                    };
                    file_path += node.text + '/';
                    return { "id" : node.id,"file_path":file_path};
                },
            },
            "check_callback": true,
        }, 
    });
    

    $('#jstree').on('select_node.jstree', function (e, data) {
        var parents = $('#jstree').jstree(true).get_path(data.node)
        var file_path = '#/'
        for(var i=0;i<parents.length-1;i++){
            file_path += parents[i] + '/'
        }
        file_path += data.node.text    
        $.get(
            '/file_manage/api/request_file_list',
            {'file_path':file_path},
            function(value){
                $('.file_item').remove()
                $('#file_list').append(value.li_ele)
                $('#file_box').append(value.div_ele)
                $('ul .file_item').hover(
                function(){
                    $(this).addClass('list-group-item-warning')
                },
                function(){
                    $(this).removeClass('list-group-item-warning')
                })
                $('.file_item').each(function(index,ele){
                    if($(ele).attr('file_type')=='dir'){
                        $(ele).dblclick(
                            request_file_list
                        )
                    }else if(["mp4","ts",].indexOf($(ele).attr('file_type'))!=-1){
                        $(ele).dblclick(
                            play_video
                        )
                    }else if(['png', 'JPG', 'jpg', 'PNG'].indexOf($(ele).attr('file_type'))!=-1){
                        $(ele).dblclick(
                            view_image
                        )
                    }
                })
                
                $('ul .file_item').click(
                    selected_list_item
                )
                $('div .file_item').click(
                    selected_box_item
                )
                
                $('.file_item').contextmenu({
                    target:'#context-menu', 
                    before: function(e,context) {
                        // execute code before context menu if shown
                    },
                    onItem: function(context,e) {
                        // execute on menu item selection
                        // click button(e.target)  select ele context[0]
                        var text = $(e.target)[0].innerText
                        if(text == 'Rename'){
                            $('#exampleModal').modal()
                            rename_click(context[0])
                        }
                    }
                })   
            },
            'json'
        )
        }).jstree(true);

    
    $('#jstree').on('rename_node.jstree', function(e, data){
        var parents = $('#jstree').jstree(true).get_path(data.node)
        var file_path = '#/'
        var old_file_path = '#/'
        data.instance.set_icon(data.node,"/static/file_manage/jstree/ico/file.ico")
        for(var i=0;i<parents.length-1;i++){
            file_path += parents[i] + '/'
            old_file_path += parents[i] + '/'
        }
        
        file_path += data.node.text
        old_file_path += data.old
        if(data.old == 'New node'){
            $.post(
                '/file_manage/api/create_dir',
                {'file_path':file_path},
                function(value){
                    //data.node.id = value.id 
                    data.old = value.dir_name
                },
                'json'
            )
        }else{
            $.post(
                '/file_manage/api/rename_dir',
                {'file_path':file_path,'old_file_path':old_file_path},
                function(value){
                    //data.node.id = value.id 
                    data.old = value.dir_name
                },
                'json'
            )
        }

        }).jstree(true);
    $('#jstree').on('delete_node.jstree', function (e, data) {
        var parents = $('#jstree').jstree(true).get_path(data.node)
        var file_path = '#/'
        for(var i=0;i<parents.length-1;i++){
            file_path += parents[i] + '/'
        }
        file_path += data.node.text
        $.post(
            '/file_manage/api/delete_dir',
            {'file_path[]':[file_path,]},
            function(value){
            },
            'json'
        )             
        }).jstree(true);
    var last_path = null
    function request_file_list(){
        var file_path = $(this).attr('file_path')
        $.get(
            '/file_manage/api/request_file_list',
            {'file_path':file_path},
            function(value){
                $('.file_item').remove()
                $('#file_list').append(value.li_ele)
                $('#file_box').append(value.div_ele)
                $('ul .file_item').hover(
                function(){
                    $(this).addClass('list-group-item-warning')
                },
                function(){
                    $(this).removeClass('list-group-item-warning')
                })
                $('.file_item').each(function(index,ele){
                    if($(ele).attr('file_type')=='dir'){
                        $(ele).dblclick(
                            request_file_list
                        )
                    }else if(["mp4","ts",].indexOf($(ele).attr('file_type'))!=-1){
                        $(ele).dblclick(
                            play_video
                        )
                    }else if(['png', 'JPG', 'jpg', 'PNG'].indexOf($(ele).attr('file_type'))!=-1){
                        $(ele).dblclick(
                            view_image
                        )
                    }
                })
                
                $('ul .file_item').click(
                    selected_list_item
                )
                $('div .file_item').click(
                    selected_box_item
                )
                
                $('.file_item').contextmenu({
                    target:'#context-menu', 
                    before: function(e,context) {
                        // execute code before context menu if shown
                    },
                    onItem: function(context,e) {
                        // execute on menu item selection
                        // click button(e.target)  select ele(context[0])
                        var text = $(e.target)[0].innerText
                        if(text == 'Rename'){
                            $('#exampleModal').modal()
                            rename_click(context[0])
                        }
                    }
                })   
            },
            'json'
        )
        }
    function selected_list_item(){
        if($(this).hasClass('list-group-item-info')){
            $(this).removeClass('list-group-item-info')
        }else{
            $(this).addClass('list-group-item-info')
        }
    }
    function selected_box_item(){
        if($(this).children('a').hasClass('my_active')){
            $(this).children('a').removeClass('my_active')
        }else{
            $(this).children('a').addClass('my_active')
        }
    }
    function rename_click(target){
        var old_file_name = $(target).text().trim()
        var old_file_path = $(target).attr('file_path')
        $("input[name=new_file_name]").val(old_file_name)
        $("input[name=old_file_path]").val(old_file_path)
        $(".submit_rename").click(function(){
            var rename_form = document.getElementById("renama_form")
            var input = rename_form.getElementsByTagName('input')
            var data = {}
            for(var i=0;i<input.length;i++){
                data[input[i].name]=input[i].value
            }
            $.post(
                '/file_manage/api/rename_dir',
                data,
                function(value){
                    location.reload()
                },
                'json'
            )
        })
    }
    $(".add_file").click(function(){
        $("input[name=add_new_file]").trigger("click")
        
    })
    var progressbar_value = 0
    function set_progressbar_value(){
        $( "#progressbar" ).progressbar({
            value: progressbar_value += 5
        });
    }
    $("input[name=add_new_file]").change(function(){
        var file =  $(this)[0].files
        var formData = new FormData();
        for(var i=0;i<file.length;i++){
            formData.append(file[i].name,file[i])
        }
        var file_path  = $('#jstree').jstree(true).get_selected()
        formData.append('file_path', file_path)
        $('#modale_back').css("display", "block");
        $('#progressbar').css("display", "block")
        var i = setInterval(set_progressbar_value,1000);
        $.ajax({
            type:'post',
            url:"/file_manage/api/add_files",
            data:formData,
            dataType:'json',
            contentType:false,
            processData:false,
            success:function(data){
                clearInterval(i)
                location.reload()
			}
        })
    })
    var video_obj = null
    
    $('.video_close_button').hover(
        function(){
            $(this).css('background-color','darkgray')
        },
        function(){
            $(this).css('background-color','')
        }
    )
    $('.video_close_button').click(
        function(){
            $('#modale_back').css("display", "none");
            $('#video_box').css("display", "none");
            $('#image_box').css('display', 'none')
            
        }
    )
    $('.delete_button').click(
        function(){
            var file_item = null
            var item_type = null
            var delete_path_list = []
            if($('#file_list').css('display') != 'none'){
                file_item = $('#file_list').children()
                for(var i=0;i<file_item.length;i++){
                    if($(li[i]).hasClass('list-group-item-info')){
                        delete_path_list.push($(li[i]).attr('file_path'))
                    }
                }
            }else{
                file_item = $('#file_box').children()
                for(var i=0;i<file_item.length;i++){
                    if($(file_item[i]).children('a').hasClass('my_active')){
                        delete_path_list.push($(file_item[i]).attr('file_path'))
                    }
                }
            }
            if(delete_path_list.length>0){
                $('#can_delete').modal()
                $('.delete_file').click(function(){
                    $.post(
                        '/file_manage/api/delete_dir',
                        {'file_path[]':delete_path_list},
                        function(data){
                            location.reload()
                        },
                        'json'
                    )
                })
            }
            
            
        }
    )
    function request_page_mode(){
        $.get(
            '/file_manage/api/request_page_mode',
            function(data){
                var page_mode = data.data.page_mode
                if(page_mode == 'List'){
                    $('#file_box').attr('style','display:none;')
                    $('#file_list').attr('style','display:block;')
                }else{
                    $('#file_list').attr('style','display:none;')
                    $('#file_box').attr('style','display:block;')
                }
            },
            'json'
        )
    };
   
    $('.view_mode').click(function(){
        var view_mode = $(this).text()
        $.post(
            '/file_manage/api/request_page_mode',
            {'mode':view_mode},
            function(data){
                location.reload()   
            },
            'json'
        )
    });

    $('.btn-info').click(function(){
        $('#file_path_choices').modal()
        $('#move_jstree').jstree({ 
            "plugins" : ['unique', 'state'],
            'core' : {
                'data' : {
                    "url" : "/file_manage/api/request_file_tree?lazy",
                    "data" : function (node) {
                        var parents = $('#move_jstree').jstree(true).get_path(node)
                        var file_path = '#/';
                        for(var i=0;i<parents.length-1;i++){
                            file_path += parents[i] + '/';
                        };
                        file_path += node.text + '/';
                        return { "id" : node.id,"file_path":file_path};
                    },
                },
                "check_callback": true,
            }, 
        });

    })
    $('#move_jstree').on('select_node.jstree', function (e, data) {
        var parents = $('#jstree').jstree(true).get_path(data.node)
        var file_path = '#/'
        for(var i=0;i<parents.length-1;i++){
            file_path += parents[i] + '/'
        }
        file_path += data.node.text
        var file_path_list = []    
        var file_list_display = $('#file_list').css('display')
        if(file_list_display=='none'){
            var div =  $('#file_box').children()
            for(var i=0;i<div.length;i++){
                if($(div[i]).children('a').hasClass('my_active')){
                    file_path_list.push($(div[i]).attr('file_path'))
                }
            }
        }else{
            var li = $('#file_list').children()
            for(var i=0;i<li.length;i++){
                if($(li[i]).hasClass('list-group-item-info')){
                    file_path_list.push($(li[i]).attr('file_path'))
                }
            }
        }
        if(file_path_list.length>0){
            $('.submit_mv_dir').click(
            function(){
                $('#modale_back').css("display", "block");
                $('#progressbar').css("display", "block")
                var i = setInterval(set_progressbar_value,1000);
                $.post(
                '/file_manage/api/mv_dir',
                {'new_path':file_path,'file_path_list[]':file_path_list},
                function(data){
                    if(data.return_code=='SUCCESS'){
                        clearInterval(i)
                        location.reload()
                    }else{
                        $('#return_msg_box p').text(data.return_msg)
                        $('#return_msg_box').modal()
                    }
                    
                },
                'json'
            )
            }
        )
        }
        
        
        }).jstree(true);
    
    
    $('.select_all_button').click(function(){
        var view_mode = $('#file_list').css('display')
        if(view_mode != 'none'){
            $('ul .file_item').addClass('list-group-item-info')
        }else{
            $('div .file_item').children('a').addClass('my_active')
        }
    })

    $('.unselect_all_button').click(function(){
        var view_mode = $('#file_list').css('display')
        if(view_mode != 'none'){
            $('ul .file_item').removeClass('list-group-item-info')
        }else{
            $('div .file_item').children('a').removeClass('my_active')
        }
    })

    function play_video(){
        var video_path = $(this).attr('file_server_path')
        $('#modale_back').css("display", "block");
        $('#video_box').css("display", "block");
        $('#my_video_1').children().attr('src',video_path)
        var video_obj = videojs('my_video_1');
        video_obj.play();
    }

    function view_image(){
        $('#modale_back').css('display','block')
        $('#image_box').children('img').attr('src',$(this).attr('file_server_path'))
        $('#image_box').css('display','block')
    }
     
    function init_page(){
        request_page_mode()
    };
    init_page();    
    
});