#coding:utf-8
from django.shortcuts import render
from app.models import Box,Parts
from app.data import * 
from django.views.decorators.cache import cache_page
from datetime import *
import json
# Create your views here.
def index(request):
    return render(request,'index.html')

#@cache_page(60 * 15)
def we30(request):

    data = make_data(Box,box='WE30')

    return render(request,'we30.html',{'data':json.dumps(data)})

#@cache_page(60 * 15)
def we30p(request):

    data = make_data(Box,box='WE30P')

    return render(request,'we30p.html',{'data':json.dumps(data)})

#@cache_page(60 * 15)
def we30c(request):

    data = make_data(Box,box='WE30C')

    return render(request,'we30c.html',{'data':json.dumps(data)})

def we30v(request):

    data = make_data(Box,box='WE30V')

    return render(request,'we30v.html',{'data':json.dumps(data)})

#@cache_page(60 * 15)
def parts(request):
    voice = make_parts_data(Parts,'语音遥控器')
    tel = make_parts_data(Parts,'2.4G遥控器')
    power_j = make_parts_data(Parts,'佳的美电源头')
    powe_t = make_parts_data(Parts,'天宝电源头')
    line = make_parts_data(Parts,'电源线')
    HDMI = make_parts_data(Parts,'HDMI线')
    av = make_parts_data(Parts,'AV线')

    return render(request, 'parts.html', {
        'voice': voice['all'],
        'voice_new': voice['new'],
        'tel': tel['all'],
        'tel_new': tel['new'],
        'power_j': power_j['all'],
        'power_j_new': power_j['new'],
        'power_t': powe_t['all'],
        'power_t_new': powe_t['new'],
        'HDMI': HDMI['all'],
        'HDMI_new': HDMI['new'],
        'line': line['all'],
        'line_new': line['new'],
        'av': av['all'],
        'av_new': av['new'],
        })
