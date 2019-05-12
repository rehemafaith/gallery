from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'photo/photos.html')


def about(request):
    return render(request,'photo/zoom.html')  