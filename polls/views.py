# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#####
from django.http import HttpResponse,Http404 , HttpResponseRedirect
from django.shortcuts import render , get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic
#####
from django.utils import timezone
from .models import Question , Choice 

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    contex = {'latest_question_list':latest_question_list}
    
    return render(request , 'polls/index.html' , contex )

'''def detail(request , question_id ):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not Exist.")

    return render(request , 'polls/detail.html' , {'question' : question })'''

def detail(request , pk):
    question = get_object_or_404(Question , pk = pk)
    return render(request , 'polls/detail.html' , {'question':question})
 
def results(request , pk):
    results = "You're looking at the results of question %s."
    return HttpResponse(results % pk)
    
def vote(request , question_id):
    question = get_object_or_404(Question , pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError , Choice.DoesNotExist):
        return render(request , 'polls/detail.html' , {
            'question':question,
            'error_message':"You didn't select a choice.",
        })   
    else:
        selected_choice.votes += 1 
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results' , args= (question.id,)))

##################################################################################################
##################################################################################################
##################################################################################################

class IndexVeiw(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailVeiw(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'  #<app name>/<model name>_detail.html


class ResulstVeiw(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

