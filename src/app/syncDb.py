'''
Created on 2015-7-2

@author: Administrator
'''
from person.models import Employee
from parts.models import Part,ConsumeRecord,IncomingRecord

records = ConsumeRecord.objects.all()
for r in records:
    r.part.owner = r.owner
    r.part.lastUpdateDateTime = r.createdAt
    r.part.save()
    
    inr = IncomingRecord(owner=r.owner,part=r.part,amount=r.amount,createdAt=r.createdAt)
    inr.save()