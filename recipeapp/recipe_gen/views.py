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
    context = { 
        'image': image
        }
    return render(request, 'image.html', context)

def results(request, id):
    image = ingredient_images.objects.get(id=id)
    path = image.ingredient_image.url
    items, file = OBJ_DET.detect(path, id)
    results = numerated_results(items)
    path = f"/output_images/{id}/{file}"
    print(path)
    context = {
        'results':results,
        'path': path,
    }
    
    return render(request, 'results.html', context)

def delete_image(request):
    images = ingredient_images.objects.all()
    images.delete()
    shutil.rmtree('./media/images')
    return redirect("/")

def back(request):
    return redirect("/")

def counter(word, list):
    count = 0
    for i in list:
        if i==word:
            count+=1
        else:
            pass
    return count

def listify(set):
    list = []
    for i in set:
        list.append(i)
    return list

def numerated_results(list):
    count_list = []
    results = []
    set_items = set(list)
    unique_items= listify(set_items)
    for item in set_items:
        count_list.append(counter(item, list))
    for i in range(0, len(set_items)):
        result = [unique_items[i],count_list[i]]
        results.append(result)
    return results