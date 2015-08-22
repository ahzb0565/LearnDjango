from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django import forms

from .models import ExecutionPlan, TestCase

# Create your views here.
def result(request, plan_id):
    plan = get_object_or_404(ExecutionPlan, pk = plan_id)
    #return HttpResponse("You're looking at result %s"%str(plan))
    return render(request, 'bob/result.html', {'plan': plan})

def index(request):
    plans = ExecutionPlan.objects.all()
    return render(request, 'bob/index.html',{'plans': plans})

def result_uploader(request):
    if request.method == "POST":
        csv_form = CsvUploadForm(request.POST, request.FILES)
        if csv_form.is_valid():
            exec_plan = csv_result_loader(request.POST, request.FILES)
            return render(request, 'bob/result.html', {'plan': exec_plan}) 
    else:
        csv_form = CsvUploadForm()
    return render(request, 'bob/result_uploader.html', {'csv_form': csv_form})
    #return render(request, 'bob/result_uploader.html',{})


class CsvUploadForm(forms.Form):
    Platform = forms.CharField()
    Image = forms.CharField()
    Domain = forms.CharField()
    #csv_name = forms.CharField()
    csv_file = forms.FileField()

def csv_result_loader(post_data, csv_file):
    platform = post_data.get('Platform')
    build_img = post_data.get('Image')
    domain = post_data.get('Domain')
    ep = ExecutionPlan(platform = platform, build_img = build_img, domain = domain)
    ep.save()
    #Need to add parser of csv result and create testcase set.
    #with open(csv_file) as csv_data:
    #    for line in csv_data:
    #        testcase = ep.testcase_set.create(xxxx)
    #        testcase.save()
    return ep
