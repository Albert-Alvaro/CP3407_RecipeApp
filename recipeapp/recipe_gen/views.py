from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .yolo import *
import shutil
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ImageForm()
    context = {
        'form': form
    }
    return render(request, 'index.html', context)

def images(request):
    image = ingredient_images.objects.all()
    for n in image:
        print(n.ingredient_image)
    context = { 'image': image}
    return render(request, 'image.html', context)

def results(request, id):
    image = ingredient_images.objects.get(id=id)
    path = image.ingredient_image.url
    items = OBJ_DET.detect(path)
    context = {
        'items': items
    }
    
    return render(request, 'results.html', context)

def delete_image(request):
    images = ingredient_images.objects.all()
    images.delete()
    shutil.rmtree('./media/images')
    return redirect("/")

def back(request):
    return redirect("/")