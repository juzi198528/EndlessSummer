# -*- coding: utf-8 -*-
'''
Created on 2015-6-13

@author: Administrator
'''
import csv
from person.models import Employee
from parts.models import Part,ConsumeRecord
from datetime import date as date

def transfer(utf8_data,owner, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, delimiter=',',dialect=dialect, **kwargs)
    for row in csv_reader:
        month = row[0]
        date = row[1]
        part_name = unicode(row[2], 'utf-8')
        unit = unicode(row[3], 'utf-8')
        amount = int(row[4])
        price = float(row[5])
        employ_name = unicode(row[9], 'utf-8')
        note = unicode(row[10], 'utf-8')
        
        part = create_part(part_name,unit,price)
        employee = load_person(employ_name)
        record = create_record(part,amount,employee,note,month,date,owner)
        record.save()
        print record

def create_part(name,unit,price):
    part = Part(name=name,price=price,unit=unit)
    part.save()
    return part

def load_person(name):
    if len(name.strip()) > 0:
        return Employee.objects.get(name=name)

def create_record(part,amount,employee,note,month,date,owner):
    createAt = build_date(month,date)
    record = ConsumeRecord(part=part,consumer=employee,amount=amount,createdAt=createAt,note=note,owner=owner)
    return record

def build_date(month,_date):
    print month
    print _date
    return date(2015, int(month), int(_date))

owner = Employee.objects.get(name=u'王怀兵')
filename = '/home/ziegler/endlessSummer/datas.csv'
transfer(open(filename),owner)

owner = Employee.objects.get(name=u'周国太')
filename = '/home/ziegler/endlessSummer/datas-2.csv'
transfer(open(filename),owner)