from django.shortcuts import render

def vistaUno(request):
    return render(request, 'app1/vista1.html')

def vistaDos(request):
    return render(request, 'app1/vista2.html')

# Create your views here.
