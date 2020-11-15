from django.shortcuts import render
from .models import Project
# Create your views here.

def ProjectsIndex(request):
    o_Projects = Project.objects.all()
    ctx = {
        'o_Projects': o_Projects
    }
    return render(request, 'ProjectsIndex.html', ctx)

def ProjectsDetail(request, pk):
    o_Project = Project.objects.get(pk=pk)
    ctx = {
        'o_Project': o_Project
    }
    return render(request, 'ProjectsDetail.html', ctx)
