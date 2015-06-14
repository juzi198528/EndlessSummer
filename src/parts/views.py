# -*- coding: utf-8 -*-
'''
Created on 2015-5-30

@author: Administrator
'''
from django.shortcuts import render_to_response, redirect
from parts.models import Part,ConsumeRecord
from person.models import Employee
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    owners = Employee.objects.filter(category=3)
    persons = Employee.objects.filter(~Q(category=3))
    return render_to_response('parts/index.html',{'persons':persons,'owners':owners})

def loadAll(request):
    records = ConsumeRecord.objects.all().order_by('-createdAt')
    totalPrice = getTotalPrice(records)
    return render_to_response('parts/records_json.html',{'records':records,'totalPrice':totalPrice})

def search(request):
    queries = []
    if request.GET.has_key('startDate') and len(request.GET['startDate'].strip()) > 0:
        startDate = datetime.datetime.strptime(request.GET['startDate'], "%Y/%m/%d")
        queries.append(Q(createdAt__gte=startDate))
    if request.GET.has_key('endDate') and len(request.GET['endDate'].strip()) > 0:
        endDate = datetime.datetime.strptime(request.GET['endDate'], "%Y/%m/%d")
        queries.append(Q(createdAt__lte=endDate))
    if request.GET.has_key('owner'):
        owner = Employee.objects.get(pk=int(request.GET['owner']))
        queries.append(Q(owner=owner))
    if request.GET.has_key('consumer'):
        consumer = Employee.objects.get(pk=int(request.GET['consumer']))
        queries.append(Q(consumer=consumer))
    if request.GET.has_key('part'):
        partName = request.GET['part']
        #parts = Part.objects.filter(name__contains=partName)
        queries.append(Q(part__name__contains=partName))
    query = Q()
    for q in queries:
        query = query & q
    records = ConsumeRecord.objects.filter(query).order_by('-createdAt')
    totalPrice = getTotalPrice(records)
    return render_to_response('parts/records_json.html',{'records':records,'totalPrice':totalPrice})

def getTotalPrice(records):
    if len(records) > 0:
        return reduce(lambda x,y:x+y, map(lambda x:x.price, records))
    return 0