
from django.http import HttpResponse
from django.template import loader

def home(request):

    template = loader.get_template('module1/home.html')
    
    return HttpResponse(template.render(request))

def fpage(request):

    template = loader.get_template('module1/fpage.html')
    return HttpResponse(template.render(request))