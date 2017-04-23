#coding:utf-8
from app.models import Box
from datetime import *


def make_data(models,box):
    result1 = ['back', 'no_question', 'factory', 'software', 'analysis', 'customer', 'rk',
               'wifi', 'mac', 'hdmi', 'power', 'tel', 'receive', ]
    result2 = ['无理由退货', '未复现问题', '工厂制程问题', '软件相关问题', '待分析', '客户应用问题',
               'RK芯片问题', 'WiFi模块问题', 'MAC错烧', 'HDMI线不良', '电源不良', '遥控器不良', '接收板不良', ]

    a = models.objects.filter(version=box).only('id')
    b = a.values('data').distinct()
    data = {}


    for x in range(len(b)):
        z= {}
        for k,j in zip(result1,result2):
            z[k] = a.filter(data=b[x]['data'],result=j).only('id').count()
            z['all'] = a.filter(data=b[x]['data']).only('id').count()
            z['hardware'] = a.filter(data=b[x]['data'],question_type='硬件').only('id').count()
            z['na'] = a.filter(data=b[x]['data'],question_type='NA').only('id').count()

        data[b[x]['data']] = z

    return data

def make_parts_data(models,type):

        model = models.objects.filter(type=type).only('type')
        dict={'new':0}
        now = datetime.now()
        for x in model:
          a = date.isoformat(x.pub_date)
          a = datetime.strptime(a,'%Y-%m-%d')
          if (now-a).days <= 7:
              dict['new'] += 1

        dict['all'] = model.filter(question_type='硬件').only('question_type').count()

        return dict

