from django.shortcuts import render
import os
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from common.Define import RETURN_CODE
from django.core import serializers
import shutil
from concurrent.futures import ThreadPoolExecutor
# Create your views here.


base_dir = settings.BASE_DIR
media_base_dir = os.path.join(base_dir,'media')


def request_file_tree(request):
    if request.method == "GET":
        GET = request.GET.get
        file_id = GET('id')
        data_list = []
        file_path = None
        if file_id == "#":
            file_path = media_base_dir
            file_list = os.listdir(media_base_dir)
            file_list.reverse()
        else:
            file_path = GET('file_path')
            file_path = file_path.replace('#',media_base_dir)
            file_list = os.listdir(file_path)
            file_list.reverse()
        for i in file_list:
            file_abs_dir = os.path.join(file_path, i)
            if os.path.isdir(file_abs_dir):
                data_list.append({'id':os.path.join(file_path, i),
                                  'text':i,
                                  "children":True,
                                  'icon':'/static/file_manage/jstree/ico/file.ico'})
        return JsonResponse(data_list,safe=False)


def create_dir(request):
    if request.method == "POST":
        POST = request.POST.get
        file_path = POST('file_path')
        file_path = file_path.replace('#',media_base_dir)
        if os.path.exists(file_path):
            file_path += '1'
        if os.path.basename(file_path) == "New node":
            file_path += '1'
        os.makedirs(file_path)
        dir_name = os.path.basename(file_path)
        return JsonResponse({'dir_name':dir_name,'id':file_path})


def rename_dir(request):
    if request.method == "POST":
        POST = request.POST.get
        file_path = POST('file_path')
        old_file_path = POST('old_file_path')
        new_file_name = POST('new_file_name')
        if new_file_name:
            file_path = os.path.join(os.path.dirname(old_file_path),new_file_name)
        if "#" in file_path:
            file_path = file_path.replace('#', media_base_dir)
        if "#" in media_base_dir:
            old_file_path = old_file_path.replace('#', media_base_dir)
        if os.path.exists(old_file_path):
            os.renames(old_file_path,file_path)
        dir_name = os.path.basename(file_path)
        return JsonResponse({'dir_name':dir_name,'id':file_path})




def delete_dir(request):
    if request.method == "POST":
        POST = request.POST.get
        file_path = POST('file_path')
        file_path = file_path.replace('#',media_base_dir)
        if os.path.exists(file_path):
            if os.path.basename(file_path) == "root":
                return JsonResponse({'return_code':'SUCCESS'})
            shutil.rmtree(file_path)
            return JsonResponse({'return_code':'SUCCESS'})




def request_file_list(request):
    file_type_dict = {
        "png": "glyphicon glyphicon-picture",
        "JPG" : "glyphicon glyphicon-picture",
        "jpg" : "glyphicon glyphicon-picture",
        "txt": "glyphicon glyphicon-book",
        "mp4": "glyphicon glyphicon-film",
        "ts": "glyphicon glyphicon-film",
        "dir": "glyphicon glyphicon-folder-open",
        "other" : "glyphicon glyphicon-question-sign",
    }
    file_type_image = {
        "txt": "/static/file_manage/image/file_image/text.png",
        "mp4": "/static/file_manage/image/file_image/video.png",
        "ts": "/static/file_manage/image/file_image/video.png",
        "dir": "/static/file_manage/image/file_image/file.png",
        "other" : "/static/file_manage/image/file_image/other.png",
    }
    if request.method == "GET":
        GET = request.GET.get
        file_path = GET('file_path')
        server_path = None
        if "#" in file_path:
            server_path = file_path.replace('#', '/media')
            file_path = file_path.replace('#', media_base_dir)
        else:
            server_path = file_path.replace(media_base_dir, '/media')
        data = {
            'li_ele':'',
            'div_ele':'',
        }
        li_ele = """
        <li class="list-group-item file_item" file_type="{0}" file_path="{1}">
            <span class="{2}"></span> {3}
        </li>
        """
        div_ele = """
        <div class="col-xs-6 col-md-2 file_item" file_type="{0}" file_path="{1}">
            <a class="thumbnail" style="text-align: center;">
            <img src="{2}" alt="..." style="max-height: 72.8px;">
            {3}
            </a>
        </div>
        """
        img_ele = '<img src="{0}" height="200px" width="200px" style="display:none;position:fixed;z-index: 1001;">'
        if os.path.exists(file_path):
            file_list = os.listdir(file_path)
            for i in file_list:
                file_abs_dir = os.path.join(file_path,i)
                if os.path.isdir(file_abs_dir):
                    data['li_ele'] += li_ele.format("dir", file_abs_dir, file_type_dict['dir'], i)
                    data['div_ele'] += div_ele.format("dir", file_abs_dir, file_type_image['dir'], i)
                elif '.' in i and i.split('.')[1] in file_type_dict:
                    if i.split('.')[1] in ['mp4','ts',]:
                        data['li_ele'] += li_ele.format(i.split('.')[1], server_path+"/" + i, file_type_dict[i.split('.')[1]], i)
                        data['div_ele'] += div_ele.format(i.split('.')[1], server_path+"/" + i, file_type_image[i.split('.')[1]], i)
                    else:
                        data['li_ele'] += li_ele.format(i.split('.')[1], file_abs_dir, file_type_dict[i.split('.')[1]], i)
                        if i.split('.')[1] in ['png','JPG','jpg']:
                            data['div_ele'] += div_ele.format(i.split('.')[1], file_abs_dir, file_abs_dir.replace(base_dir,'').replace('\\','/'), i)
                            img_path = server_path+"/"+i
                            data['li_ele'] += img_ele.format(img_path)
                else:
                     data['li_ele'] += li_ele.format("other", file_abs_dir, file_type_dict['other'], i)
                     data['div_ele'] += div_ele.format("other", file_abs_dir, file_type_image['other'], i)
        return JsonResponse(data)



def write_file(file_path, file_obj):
        with open(file_path,'wb')as w:
            for chunk in file_obj.chunks():
                w.write(chunk)


def add_files(request):
    return_value = {
        'return_code':RETURN_CODE.SUCCESS,
        'return_msg':'',
        'datas':'',
    }
    try:
        FILES = request.FILES
        POST = request.POST.get
        file_dir_name = POST('file_path')
        with ThreadPoolExecutor(max_workers=10) as pool:
            for k, v in FILES.items():
                w_file_path = os.path.join(file_dir_name, k)
                pool.submit(write_file,**{'file_path':w_file_path, 'file_obj':v})
        return JsonResponse(return_value)

    except Exception as error:
        
        return_value['return_code'] = RETURN_CODE.FAIL
        return_value['return_msg'] = "服务器出错，错误：{0}".format(error)
        return JsonResponse(return_value)



def request_page_mode(request):
    import json
    page_mode = None
    if request.method == 'GET':
        with open(base_dir+'/static/file_manage/page_conf.json', 'r')as f:
            page_mode = json.load(f)
        return JsonResponse({'data':page_mode})
    else:
        mode = request.POST.get('mode')
        with open(base_dir+'/static/file_manage/page_conf.json', 'w')as f:
            json.dump({'page_mode':mode},f)
        return JsonResponse({})

