from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import *

## Create your views here.


## For Topic
def display_topic(request):
    TMFO = TopicModelForm()
    d = {'TMFO':TMFO}

    if request.method == 'POST':
        TMFOD = TopicModelForm(request.POST)
        if TMFOD.is_valid():
            TMFOD.save()
            return HttpResponse("<center><h1 style='color:blue;'> Topic Data Inserted</h1></center>")
        else:
            return HttpResponse("<script>alert('Invalid Data Inserted...')</script>")
    return render(request, 'insert_topic.html',d)



## For Webpage
def display_webpage(request):
    WMFO = WebpageModelForm()
    d = {'WMFO':WMFO}

    if request.method == 'POST':
        WMFOD = WebpageModelForm(request.POST)
        if WMFOD.is_valid():
            WMFOD.save()
            return HttpResponse("<center><h1 style='color:blue;'> Webpage Data Inserted</h1></center>")
        else:
            return HttpResponse("<script>alert('Invalid Data Inserted...')</script>")
    return render(request, 'insert_webpage.html',d)




## For Access_Record
def display_access_record(request):
    ARMFO = Access_RecordModelForm()
    d = {'ARMFO':ARMFO}

    if request.method == 'POST':
        ARMFOD = Access_RecordModelForm(request.POST)
        if ARMFOD.is_valid():
            ARMFOD.save()
            return HttpResponse("<center><h1 style='color:blue;'> Access Record Data Inserted</h1></center>")
        else:
            return HttpResponse("<script>alert('Invalid Data Inserted...')</script>")
    return render(request, 'insert_access_record.html',d)