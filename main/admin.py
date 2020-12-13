from django.contrib import admin
from .models import Courses, Instructors


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ['id', 'title']


@admin.register(Instructors)
class InstructorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ['id', 'name',]
# Register your models here.
