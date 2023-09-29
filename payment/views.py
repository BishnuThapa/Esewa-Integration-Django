from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')

def success(request):
    return render(request,'success.html')

def fail(request):
    return render(request,'fail.html')