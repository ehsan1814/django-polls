# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Question,Choice

# Register your models here.
#new added for admin in the local host
admin.site.register(Choice)

#replace this line with this class
#admin.site.register(Question)  
class QuestionAdmin(admin.ModelAdmin):
#   fields = ['pub_date' , 'question_text' ]
   fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question , QuestionAdmin)
