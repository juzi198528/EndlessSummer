# -*- coding: utf-8 -*-
'''
Created on 2015-6-1

@author: Administrator
'''
from django.shortcuts import render_to_response, redirect
from django.views.decorators.http import require_GET,require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as authLogin, logout as authLogout
import messages
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt


def login(request):
    if request.user.is_authenticated():#logon already
        return redirect('/')
    return render_to_response('login.html')

def logout(request):
    authLogout(request)
    return redirect('/login')

@require_POST
@csrf_exempt
def doLogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        authUser = authenticate(username=username, password=password)
        if authUser is not None:
            if authUser.is_active:
                authLogin(request, authUser)
                return redirect('/')
    except Exception, e:
        errorMessage = messages.SYSTEM_ERROR
    return render_to_response('login.html', {'errorMessage':messages.INVALID_USERNAME_OR_PASSWORD})

@login_required()
def index(request):
    return render_to_response('index.html')