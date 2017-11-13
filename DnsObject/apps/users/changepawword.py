# -*- coding: utf-8 -*-
from users.forms import ChangepwdForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate

def changepwd(request):
    if request.method == 'GET':
        form = ChangepwdForm()
        return render_to_response('changepwd.html', RequestContext(request, {'form': form, }))
    else:
        form = ChangepwdForm(request.POST)
        if form.is_valid():
            username = request.user.username
            oldpassword = request.POST.get('oldpassword', '')
            user = authenticate(username=username, password=oldpassword)
            if user is not None and user.is_active:
                newpassword = request.POST.get('newpassword1', '')
                user.set_password(newpassword)
                user.save()
                return render_to_response('changepwd.html', RequestContext(request, {'changepwd_success': True}))
            else:
                return render_to_response('changepwd.html', RequestContext(request, {'form': form, 'oldpassword_is_wrong': True}))
        else:
            return render_to_response('changepwd.html', RequestContext(request, {'form': form, }))