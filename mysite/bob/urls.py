from django.conf.urls import url

from . import views

urlpatterns = [
    #Index, list all executed results
    url(r"^$", views.index, name = 'index'),
    #Execution Plan Result
    url(r"^(?P<plan_id>[0-9]+)/$", views.result, name = 'result'),
    ]
