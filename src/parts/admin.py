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

class PartAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount','price','unit')
    search_fields = ['name']

class PartConsumeRecordAdmin(admin.ModelAdmin):
    list_display = ('part', 'amount','price','consumer','createdAt','note')
    search_fields = ['name','consumer']

admin.site.register(Part,PartAdmin)
admin.site.register(ConsumeRecord,PartConsumeRecordAdmin)
