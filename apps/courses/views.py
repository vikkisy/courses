# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.messages import error
from models import Course

def index(request):
    context = {
        "courses": Course.objects.all(),
    }
    return render(request, 'courses/index.html', context)

def add(request):
    errors = Course.objects.validation(request.POST)
    if errors:
        for err in errors:
            error(request, err)
    else:
        Course.objects.create(
        name=request.POST['name'], desc=request.POST['desc'])
    return redirect('/courses')

def destroy(request, course_id):
    context = {
        "course": Course.objects.get(id=course_id)
    }
    return render(request, 'courses/destroy.html', context)

def delete(request, course_id):
        Course.objects.get(id=course_id).delete()
        return redirect('/')

# Create your views here.
