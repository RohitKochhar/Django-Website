from django.shortcuts import render

# Create your views here.

def AboutIndex(request):
    return render(request, "Landing.html")
