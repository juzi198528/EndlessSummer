# -*- coding: utf-8 -*-
'''
Created on 2015-6-4

@author: Administrator
'''
'''
Created on Apr 5, 2013

@author: zhangwuh
'''
from django.contrib import admin
from models import *

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile','category')
    search_fields = ['name','mobile']
    list_filter = ('category',)


admin.site.register(Employee,EmployeeAdmin)
