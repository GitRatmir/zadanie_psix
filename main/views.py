from django.shortcuts import render
from django.http import HttpResponseGone


def index(request):
    return HttpResponseGone('Ратмир')

# Create your views here.
