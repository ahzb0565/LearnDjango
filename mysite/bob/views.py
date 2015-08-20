from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import ExecutionPlan, TestCase

# Create your views here.
def result(request, plan_id):
    plan = get_object_or_404(ExecutionPlan, pk = plan_id)
    #return HttpResponse("You're looking at result %s"%str(plan))
    return render(request, 'bob/result.html', {'plan': plan})

def index(request):
    plans = ExecutionPlan.objects.all()
    return render(request, 'bob/index.html',{'plans': plans})
