from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def simple_view(request):
    return render(request, 'first_app/example.html')
