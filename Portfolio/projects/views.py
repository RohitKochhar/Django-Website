from django.shortcuts import render
from .models import Project
# Create your views here.

def Index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'Index.html', context)

def ProjectDetail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'ProjectDetail.html', context)
