from django.shortcuts import render

# Create your views here.

def AboutIndex(request):
    return render(request, "Landing.html")

def Profile(request):
    return render(request, "Profile.html")
