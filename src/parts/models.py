# -*- coding: utf-8 -*-

from django.db import models
from person.models import Employee

class Part(models.Model):
    class Meta:
        db_table = "parts"
        verbose_name = "修理厂零件库存记录"
        verbose_name_plural = "修理厂零件库存记录"

    name = models.CharField(verbose_name="名称", max_length=255,blank=False)
    amount = models.IntegerField(verbose_name="总消耗数量",max_length=5,blank=True,editable=False,default=0)
    price = models.FloatField(verbose_name="单价",blank=False)
    unit = models.CharField(verbose_name="单位", max_length=255,blank=False)
    note = models.TextField(verbose_name="备注",blank=True)
    lastUpdateDateTime = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.name
    
    def updateRemainingAmount(self):
        records = ConsumeRecord.objects.filter(part=self)
        _amount = 0
        for record in records:
            _amount += record.amount
        self.amount = _amount
        self.save()  

class ConsumeRecord(models.Model):
    class Meta:
        db_table = "parts_consume_record"
        verbose_name = "修理厂零件消耗记录"
        verbose_name_plural = "修理厂零件消耗记录"
    
    owner = models.ForeignKey(Employee,verbose_name="负责人",blank=False,related_name="owner")
    consumer = models.ForeignKey(Employee,verbose_name="领取人",blank=False)
    part = models.ForeignKey(Part,verbose_name="零件",blank=False)
    amount = models.PositiveSmallIntegerField(verbose_name="数量",max_length=5,blank=False)
    createdAt = models.DateField(verbose_name="领取时间")
    price = models.FloatField(verbose_name="总价",max_length=5,editable=False)
    note = models.TextField(verbose_name="备注",blank=True)
    
    def save(self, force_insert=False, force_update=False, using=None):
        self.price = self.amount * self.part.price
        models.Model.save(self)
        self.part.updateRemainingAmount()
    def __unicode__(self):
        return self.part.name + u'消耗记录'
