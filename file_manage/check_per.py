from django.core.urlresolvers import resolve
from django.shortcuts import render, redirect
from file_manage.permission_list import perm_dict
from django.conf import settings


def perm_check(*args, **kwargs):
    request = args[0]
    resolve_url_obj = resolve(request.path)
    current_url_name = resolve_url_obj.url_name
    match_results = [None]
    match_key = None
    if request.user.is_authenticated() is False:
        return redirect(settings.LOGIN_URL)

    for permission_key, permission_val in perm_dict.items():

        per_url_name = permission_val[0]
        per_method = permission_val[1]
        perm_args = permission_val[2]
        perm_kwargs = permission_val[3]
        perm_hook_funk = permission_val[4] if len(permission_val) > 4 else None

        if current_url_name in per_url_name:
            if request.method in per_method:
                args_matched = False
                for item in perm_args:
                    request_method_fuc = getattr(request, per_method)
                    if request_method_fuc.get(item):
                        args_matched = True
                    else:
                        args_matched = False
                        break
                else:
                    args_matched = True
                kwargs_matched = False
                for k, v in perm_kwargs.items():
                    request_method_fuc = getattr(request, per_method)
                    arg_val = request_method_fuc.get(k)
                    if arg_val == str(v):
                        kwargs_matched = True
                    else:
                        kwargs_matched = False
                        break

                else:
                    kwargs_matched = True

                perm_hook_matched = False
                if perm_hook_funk:
                    perm_hook_matched = perm_hook_funk(request)
                else:
                    perm_hook_matched = True

                match_results = [
                    args_matched, kwargs_matched, perm_hook_matched
                ]
                if all(match_results):
                    match_key = permission_key
                    break
    if all(match_results):
        perm_obj = match_key.replace('/','.')
        if request.user.has_perm(perm_obj):
            return True

        else:  
            return False
    else:
        return False



def check_permission(func):
    def inner(*args, **kwargs):
        if not perm_check(*args, **kwargs):
            request = args[0]
            return render(request, 'file_manage/no_permission.html')
        return func(*args, **kwargs)
    return inner
