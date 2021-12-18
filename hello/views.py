from django.http import HttpResponse
from django.template import loader


def index(request):
    context = None
    template = loader.get_template('hello/index.html')
    return HttpResponse(template.render(context, request))


def resume(request):
    context = None
    template = loader.get_template('hello/resume.html')
    return HttpResponse(template.render(context, request))


def contact(request):
    context = None
    template = loader.get_template('hello/contact.html')
    return HttpResponse(template.render(context, request))
