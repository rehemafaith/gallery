from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image
 


def home(request):
    image = Image.objects.all()

  

    return render(request,'photo/photos.html',{"image":image})


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(category)
        message = f"{category}"

        return render(request, 'photo/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any images"
        return render(request, 'photo/search.html',{"message":message})