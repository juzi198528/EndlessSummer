# -*- coding: utf-8 -*-
'''
Created on 2015-6-4

@author: Administrator
'''
from django.db import models

class Employee(models.Model):
    class Meta:
        verbose_name = '人员信息'
        verbose_name_plural = '人员信息'
    DRIVER = 1
    REPAIR = 2
    OTHER = 3
    CATEGORIES = (
         (DRIVER, '司机'),
         (REPAIR, '修理工'),
         (OTHER, '其他')
    )
    name = models.CharField(max_length=40,verbose_name="姓名",blank=False)
    mobile = models.CharField(max_length=13,verbose_name="手机号",blank=True)
    category = models.IntegerField(verbose_name="类别",max_length=1,choices=CATEGORIES)

    def __unicode__(self):
        return self.name