from django.shortcuts import render
from .models import Courses, Instructors
from django.http import HttpResponseGone


def index(request):
    courses = Courses.objects.all()
    context = {
        'courses':courses,
    }
    return render(request,'main/index.html', context)

# Create your views here.
