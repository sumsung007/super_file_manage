$(function(){
    $('#page1').addClass('active')
    function init_user_table(){
        $.get(
            '/file_manage/api/request_user_list',
            function(data){
                var data_list = data.data
                $('#user_data_list').children().remove()
                $('#user_data_list').append(data_list)
                $('.user_item').contextmenu({
                    target:'#context-menu', 
                    before: function(e,context) {
                        // execute code before context menu if shown
                    },
                    onItem: function(context,e) {
                        // execute on menu item selection
                        // click button(e.target)  select ele context[0]
                        var text = $(e.target)[0].innerText
                        if(text == 'RePassword'){
                            $('#change_password_modal').modal()
                            $('#change_password_modal input[name=id]').val($(context[0]).attr('user_id'))
                        }
                    }
                })
                $('.submit_repassword').click(function(){
                    var $form_input = $('#change_password_modal input')
                    var data = {}
                    $form_input.each(function(index,ele){
                        data[$(ele).attr('name')]=$(ele).val()
                    })
                    $.post(
                        '/file_manage/api/change_password',
                        data,
                        function(rsp){
                            if(rsp.return_code=='SUCCESS'){
                                $form_input.each(function(index,ele){
                                    if($(ele).attr('name')!='id'){
                                        $(ele).val('')
                                    }
                                })
                                $('#change_password_modal').modal('hide')
                            }else{
                                $('#change_password_modal').modal('hide')
                                $('#return_msg_box p').text(rsp.return_msg)
                                $('#return_msg_box').modal()
                            }
                            
                        },
                        'json'
                    )
                })   
                $('.user_item').click(function(){
                    $(this).siblings().removeClass('active')
                    $(this).addClass('active')
                    $.get(
                        '/file_manage/api/update_user',
                        {'user_id':$(this).attr('user_id')},
                        function(data){
                            $('.user_info_box').css('display','block')
                            var $input = $('.user_info_box input')
                            $input.each(function(index,ele){
                                $(ele).val(data.data[$(ele).attr('name')])
                                if($(ele).attr('name') != 'id'){
                                    $(ele).attr('old_data',data.data[$(ele).attr('name')])
                                }
                            })
                            var is_super_user = data.data['is_superuser'] ? 'OP' : 'OF'
                            if(is_super_user == 'OP'){
                                $('.user_info_box .super_user_button').removeClass('btn-danger')
                                $('.user_info_box .super_user_button').addClass('btn-success')
                                $('.user_info_box .super_user_button').text('OP')
                                $('.user_info_box .super_user_button').attr('old_data','OP')
                            }else{
                                $('.user_info_box .super_user_button').removeClass('btn-success')
                                $('.user_info_box .super_user_button').addClass('btn-danger')
                                $('.user_info_box .super_user_button').text('OF')
                                $('.user_info_box .super_user_button').attr('old_data','OF')
                            }
                            var is_login = data.data['is_active'] ? 'OP' : 'OF'
                            if(is_login == 'OP'){
                                $('.user_info_box .can_login_button').removeClass('btn-danger')
                                $('.user_info_box .can_login_button').addClass('btn-success')
                                $('.user_info_box .can_login_button').text('OP')
                                $('.user_info_box .can_login_button').attr('old_data','OP')
                            }else{
                                $('.user_info_box .can_login_button').removeClass('btn-success')
                                $('.user_info_box .can_login_button').addClass('btn-danger')
                                $('.user_info_box .can_login_button').text('OF')
                                $('.user_info_box .can_login_button').attr('old_data','OF')
                            }
                            $('.user_info_box .my_select').multiSelect('deselect_all');
                            $('.user_info_box .my_select').multiSelect('select',data.permission_list)
                            $('.user_info_box_commit').click(function(){
                                var $input = $('.user_info_box input')
                                var formData = new FormData()
                                $input.each(function(index,ele){
                                    if($(ele).attr('old_data')!=$(ele).val()){
                                        formData.append($(ele).attr('name'),$(ele).val())
                                    }
                                })
                                if($('.user_info_box .super_user_button').text()!=$('.user_info_box .super_user_button').attr('old_data')){
                                    var is_super_user = ($('.user_info_box .super_user_button').text()=='OP') ? true : false
                                    formData.append('is_superuser',is_super_user)
                                }
                                if($('.user_info_box .can_login_button').text()!=$('.user_info_box .can_login_button').attr('old_data')){
                                    var is_login = ($('.user_info_box .can_login_button').text()=='OP') ? true : false
                                    formData.append('is_active',is_login)
                                }
                                formData.append($('.user_info_box .my_select').attr('name'),$('.user_info_box .my_select').val())
                                $.ajax({
                                    type:'post',
                                    url:'/file_manage/api/update_user',
                                    data:formData,
                                    dataType:'json',
                                    contentType:false,
                                    processData:false,
                                    success:function(data){
                                        if(data.return_code=='SUCCESS'){
                                            init_user_table()
                                        }else{
                                            $('#return_msg_box p').text(data.return_msg)
                                            $('#return_msg_box').modal()
                                        }
                                    }
                                })
                            })

                        },
                        'json'
                    )
                })
            },
            'json'
        )
    }
    $('.add_user_button').click(function(){
        $('#add_user_modal').modal()
        $('.submit_add_user').click(function(){
            var $form_input = $('#add_user_form input')
            var formData = new FormData();
            $form_input.each(function(index,ele){
                formData.append($(ele).attr('name'), $(ele).val())
            })
            var $form_select = $('#add_user_form select')
            $form_select.each(function(index,ele){
                formData.append($(ele).attr('name'), $(ele).val())
            })
            var super_user = $('.super_user_button').text()
            super_user = (super_user == 'OF') ? 0 : 1
            var can_login = $('.can_login_button').text()
            can_login = (can_login == 'OF') ? 0 : 1
            formData.append('is_super_user',super_user)
            formData.append('is_active',can_login)
            $.ajax({
                type:'post',
                url:'/file_manage/api/create_user',
                data:formData,
                dataType:'json',
                contentType:false,
                processData:false,
                success:function(data){
                    if(data.return_code=='SUCCESS'){
                        init_user_table()
                        $('#add_user_modal').modal('hide')
                    }else{
                        $('#return_msg_box p').text(data.return_msg)
                        $('#return_msg_box').modal()
                    }
                }
            })
        })
    })
    $('.delete_user_button').click(function(){
        var user_item = null
        $('.user_item').each(function(index,ele){
            if($(ele).hasClass('active')){
                user_item = ele
            }
            
        })
        $.post(
            '/file_manage/api/delete_user',
            {'user_id':$(user_item).attr('user_id')},
            function(data){
                if(data.return_code=='SUCCESS'){
                    init_user_table()
                    $('.user_info_box').css('display','none')
                }else{
                    $('#return_msg_box p').text(data.return_msg)
                    $('#return_msg_box').modal()
                }
            },
            'json'
        )
    })

    function init_permission_list(){
        $.get(
            '/file_manage/api/request_permission_list',
            function(data){
                var value_data = data.data
                $('.my_select').multiSelect()
                for(var i=0;i<value_data.length;i++){
                    $('.my_select').multiSelect('addOption', value_data[i])
                }
                $('.user_info_button').click(function(){
                    if($(this).text()=='OF'){
                        $(this).removeClass('btn-danger')
                        $(this).addClass('btn-success')
                        $(this).text('OP')
                    }else{
                        $(this).removeClass('btn-success')
                        $(this).addClass('btn-danger')
                        $(this).text('OF')
                    }
                })
            },
            'json'
        )
        
    }
    function init_page(){
        init_user_table()
        init_permission_list()
    }
    init_page()
})