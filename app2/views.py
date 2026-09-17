from django.shortcuts import render

def vistaTres(request):
    return render(request, 'app2/vista3.html')

def vistaCuatro(request):
    return render(request, 'app2/vista4.html')

# Create your views here.
