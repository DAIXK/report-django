from django.contrib import admin
from app.models import *
from django import forms

# Register your models here.


class BoxAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'order','name','sn','mac',
                    'question','remarks','question_type','reason',
                    'result','version','data','time')

    search_fields = ['id', 'type', 'order','name','sn','mac',
                    'question','remarks','question_type','reason',
                    'result','version','data',]

class PartsAdmin(admin.ModelAdmin):
    list_display = ('id',  'order', 'name','sn', 'question','question_type','time','type')

    search_fields = ['id', 'order', 'name', 'sn', 'question_type','type'  ]

admin.site.register(Box,BoxAdmin)
admin.site.register(Parts,PartsAdmin)
