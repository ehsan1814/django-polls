from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
# Create your views here.

def ehsan(request):
    return render(request , 'ehsan/index.html' , {'latest_question_list' : Question.objects.order_by('-pub_date')[:5] })
    #return HttpResponse('thei')