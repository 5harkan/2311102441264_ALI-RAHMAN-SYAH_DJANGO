from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    template_name = 'public/base.html'
    context = {
        'title':'my home',
        'welcome':'welcome my home',
    }
    return render(request, template_name, context)