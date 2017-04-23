# -*- coding: utf-8 -*-
from django.utils import timezone
from django.shortcuts import render
from django.conf import settings
import os
import datetime
import xlrd
from app.models import Box,Parts
import re



def upload_parts(request):
    file_obj = request.FILES.get('file', None)
    today = datetime.datetime.today()
    info = []

    if file_obj:
        file_name = 'parts-%d-%d.xlsx' % (today.month, today.day)
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        f = open(file_path, 'wb+')
        f.write(file_obj.read())
        f.close()

    data = xlrd.open_workbook('upload/parts-%d-%d.xlsx' % (today.month, today.day))
    table = data.sheets()[0]
    nrows = table.nrows
    for i in range(nrows):
        data = Parts(type=table.row_values(i)[0],order=table.row_values(i)[1],name=table.row_values(i)[2],
                                    sn=table.row_values(i)[3],question=table.row_values(i)[4],question_type=table.row_values(i)[5],pub_date=timezone.now())
        data.save()

    return render(request, 'save_parts.html', {'info': info})

def upload(request):
        file_obj = request.FILES.get('file',None)
        today = datetime.datetime.today()
        info = []


        if file_obj:
            file_name = 'webox-%d-%d.xlsx'%(today.month,today.day)
            file_path = os.path.join(settings.MEDIA_ROOT,file_name)
            f = open(file_path,'wb+')
            f.write(file_obj.read())
            f.close()

        data = xlrd.open_workbook('upload/webox-%d-%d.xlsx'%(today.month,today.day))
        table = data.sheets()[0]
        nrows = table.nrows

        for i in range(nrows):
            if len(table.row_values(i)[3]) == 15 :
                try:
                        data = Box(type=table.row_values(i)[0],order=table.row_values(i)[1],name=table.row_values(i)[2],
                                    sn=table.row_values(i)[3],mac=table.row_values(i)[4],question=table.row_values(i)[5],
                                    remarks=table.row_values(i)[6],question_type=table.row_values(i)[7],reason=table.row_values(i)[8],
                                    result=table.row_values(i)[9],version=table.row_values(i)[3][0:4],
                                    data=table.row_values(i)[3][4:10],pub_date=timezone.now(),)
                        data.save()

                except Exception as e :
                    info.append(e)
                    info.append(table.row_values(i)[3])
                    continue
            elif len(table.row_values(i)[3]) == 16:
                try:
                    data = Box(type=table.row_values(i)[0],order=table.row_values(i)[1],name=table.row_values(i)[2],
                                sn=table.row_values(i)[3],mac=table.row_values(i)[4],question=table.row_values(i)[5],
                                remarks=table.row_values(i)[6],question_type=table.row_values(i)[7],reason=table.row_values(i)[8],
                                result=table.row_values(i)[9],version=cheick(table.row_values(i)[3][0:5]),
                                data=table.row_values(i)[3][5:11],pub_date=timezone.now(),)
                    data.save()
                except Exception as e :
                    info.append(e)
                    info.append(table.row_values(i)[3])
                    continue



        return render(request,'save.html',{'info':info})


def cheick(string):
    if string[4] != str(0):
        return string[0:5]
    else:
        return string[0:4]

