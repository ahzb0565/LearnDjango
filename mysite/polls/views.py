from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader, RequestContext

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You are at the polls index")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s."%question_id)

def results(request, question_id):
    return HttpResponse("You're looking at the result of question %s."%question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s."%question_id)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([p.question_text for p in latest_question_list])
    #return HttpResponse(output)
    template = loader.get_template('polls/index.html')
    context = RequestContext(
            request,
            {'latest_question_list': latest_question_list},
        )
    return HttpResponse(template.render(context))
