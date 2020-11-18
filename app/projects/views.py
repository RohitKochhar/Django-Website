from django.shortcuts import render
from .models import Project, TechnologyUsed
# Create your views here.

def Index(request):
    o_Projects      = Project.objects.all()
    a_TechChoices   = TechnologyUsed.TechnologyChoices
    ctx = {
        'o_Projects': o_Projects,
        'a_TechChoices': a_TechChoices
    }
    return render(request, 'ProjectsIndex.html', ctx)

def Detail(request, pk):
    o_Project = Project.objects.get(pk=pk)
    ctx = {
        'o_Project': o_Project
    }
    return render(request, 'ProjectsDetail.html', ctx)

def FilterByTechnology(request):

    print(f"DEBUG: {request.POST}")
    
    # Try to load form
    s_Tech          = request.POST.get('s_TechnologySelection')
    # Pull all the technologies specified
    o_Technologies  = TechnologyUsed.objects.get(s_Name=s_Tech)
    o_Projects      = Project.objects.filter(technologies__s_Name = s_Tech)
    a_TechChoices   = TechnologyUsed.TechnologyChoices
    ctx = {
        'o_Projects': o_Projects,
        'a_TechChoices': a_TechChoices
    }
    return render(request, 'ProjectsIndex.html', ctx)
