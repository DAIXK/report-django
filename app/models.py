#coding:utf-8
from django.db import models
from django.forms import ModelForm
from django.core.files import File
from django import forms

# Create your models here.



class Box(models.Model):
    type = models.CharField(max_length=10,verbose_name=u'类型')
    order = models.CharField(max_length=40,verbose_name=u'订单号')
    name = models.CharField(max_length=40,blank=True,verbose_name=u'姓名')
    sn = models.CharField(max_length=20,unique=True,verbose_name=u'SN')
    mac = models.CharField(max_length=20,blank=True,verbose_name=u'MAC')
    question = models.CharField(max_length=300,blank=True,verbose_name=u'问题描述')
    remarks = models.CharField(max_length=20,blank=True,verbose_name=u'判断表征')
    question_type = models.CharField(max_length=5,verbose_name=u'不良类型')
    reason = models.CharField(max_length=10,verbose_name=u'根本原因')
    result = models.CharField(max_length=10,verbose_name=u'原因归类')
    version = models.CharField(max_length=10,verbose_name=u'型号')
    data = models.CharField(max_length=10,verbose_name=u'批次日期')
    pub_date = models.DateTimeField('date published')

    class Meta:
        verbose_name = '盒子数据'
        verbose_name_plural = verbose_name

    def time(self):
        return self.pub_date

    def __unicode__(self):
        return self.sn


class Parts(models.Model):
    type = models.CharField(max_length=10,verbose_name=u'类型')
    order = models.CharField(max_length=50, blank=True,verbose_name=u'订单号')
    name = models.CharField(max_length=100, blank=True,verbose_name=u'客户姓名')
    sn = models.CharField(max_length=30)
    question = models.CharField(max_length=300, blank=True,verbose_name=u'问题描述')
    question_type = models.CharField(max_length=20,verbose_name=u'不良类型')
    pub_date = models.DateTimeField('date published')


    class Meta:
        verbose_name = '配件数据'
        verbose_name_plural = verbose_name

    def time(self):
        return self.pub_date

    def __unicode__(self):
        return self.SN