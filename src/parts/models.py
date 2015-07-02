# -*- coding: utf-8 -*-

from django.db import models
from person.models import Employee

class Part(models.Model):
    class Meta:
        db_table = "parts"
        verbose_name = "修理厂零件库存记录"
        verbose_name_plural = "修理厂零件库存记录"
        ordering = ['name']
    name = models.CharField(verbose_name="名称", max_length=255,blank=False)
    price = models.FloatField(verbose_name="单价",blank=False)
    unit = models.CharField(verbose_name="单位", max_length=255,blank=False)
    note = models.TextField(verbose_name="备注",blank=True)
    lastUpdateDateTime = models.DateTimeField(auto_now=True,verbose_name="更新时间")
    owner = models.ForeignKey(Employee,verbose_name="修理厂负责人",blank=True,limit_choices_to = { 'category': 3})
   
    @property
    def remaining(self):
        incomingTotal = 0
        if self.incomingrecord_set.all():
            incomingTotal = reduce(lambda x,y:x+y, map(lambda x:x.amount, self.incomingrecord_set.all()))
        consumeTotal = 0
        if self.consumerecord_set.all():
            consumeTotal = reduce(lambda x,y:x+y, map(lambda x:x.amount, self.consumerecord_set.all()))
        return incomingTotal - consumeTotal
    
    def __unicode__(self):
        return self.name
    
class IncomingRecord(models.Model):
    class Meta:
        db_table = "parts_incoming_record"
        verbose_name = "修理厂零件入库记录"
        verbose_name_plural = "修理厂零件入库记录"
        
    owner = models.ForeignKey(Employee,verbose_name="修理厂负责人",blank=True,limit_choices_to = { 'category': 3})
    part = models.ForeignKey(Part,verbose_name="零件")
    amount = models.PositiveSmallIntegerField(verbose_name="数量",max_length=5)
    createdAt = models.DateField(verbose_name="入库时间")
    note = models.TextField(verbose_name="备注",blank=True)
    
    @property
    def price(self):
        return self.part.price * self.amount

    def __unicode__(self):
        return self.part.name + u'入库记录'

class ConsumeRecord(models.Model):
    class Meta:
        db_table = "parts_consume_record"
        verbose_name = "修理厂零件出库记录"
        verbose_name_plural = "修理厂零件出库记录"
    
    owner = models.ForeignKey(Employee,verbose_name="修理厂负责人",blank=True,related_name="owner", limit_choices_to = { 'category': 3})
    consumer = models.ForeignKey(Employee,verbose_name="领取人",blank=True,null=True,limit_choices_to = { 'category': 2})
    part = models.ForeignKey(Part,verbose_name="零件",blank=False)
    amount = models.PositiveSmallIntegerField(verbose_name="数量",max_length=5,blank=False)
    createdAt = models.DateField(verbose_name="出库时间")
    note = models.TextField(verbose_name="备注",blank=True)
    
    @property
    def price(self):
        return self.amount * self.part.price
    
    def __unicode__(self):
        return self.part.name + u'出库记录'
