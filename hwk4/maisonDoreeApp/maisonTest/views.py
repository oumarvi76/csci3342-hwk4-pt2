from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    context = {"name":"OmarVi"}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request)) # from this template project,
