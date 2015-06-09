# -*- coding: utf-8 -*-
'''
Created on 2015-5-30

@author: Administrator
'''
from django.shortcuts import render_to_response, redirect
from parts.models import Part,ConsumeRecord
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import datetime
def index(request):
    return render_to_response('parts/index.html')

def loadAll(request):
    records = ConsumeRecord.objects.all()
    return render_to_response('parts/records_json.html',{'records':records})

def search(request):
    start = request.GET['startDate']
    end = request.GET['endDate']
    startDate = datetime.datetime.strptime(start, "%Y/%m/%d")
    endDate = datetime.datetime.strptime(end, "%Y/%m/%d")
    records = ConsumeRecord.objects.filter(Q(createdAt__gte=startDate) & Q(createdAt__lte=endDate))
    return render_to_response('parts/records_json.html',{'records':records})
