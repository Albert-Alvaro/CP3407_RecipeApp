from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .yolo import *
import shutil
import json
from .llm import LLM
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

    for ing in results:
        ingredients = Ingredients()
        print(ing[0])
        ingredients.ingredient_name = ing[0]
        ingredients.save()
    context = {
        'results':results,
        'path': path,
        'id': id
    }
    
    return render(request, 'results.html', context)

def add_remove_ingredients(request, id):
    ingredients = Ingredients.objects.all()
    for i in ingredients:
        print(i.ingredient_name)
    form = IngredientForm
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form' : form,
        'ingredients': ingredients,
        'id': id
    }
    return render(request, 'add_remove_ing.html', context)

def llm_results(request):
    ingredients = Ingredients.objects.all()
    ings = []
    for i in ingredients:
        ings.append(i.ingredient_name)
    recipe = LLM.generate_recipe(ings)
    print(recipe)
    context = {
        'recipe': recipe
    }
    return render(request, 'llm_result.html', context)

def delete_image(request):
    images = ingredient_images.objects.all()
    images.delete()
    shutil.rmtree('./media/images')
    return redirect("/")

def del_back_ing(request):
    if os.path.isdir('../recipeapp/sensitive.json'):
        path = get_keys("../recipeapp/sensitive.json")
        key = path['path']   
        shutil.rmtree(f"{key}")
    else:
        pass
    ingredients = Ingredients.objects.all()
    ingredients.delete()
    return redirect(f"/images")

def back(request):
    if os.path.isdir('../recipeapp/sensitive.json'):
        path = get_keys("../recipeapp/sensitive.json")
        key = path['path']   
        shutil.rmtree(f"{key}")
    else:
        pass
    ingredients = Ingredients.objects.all()
    ingredients.delete()
    return redirect("/")

def del_back(request, id):
    if os.path.isdir('../recipeapp/sensitive.json'):
        path = get_keys("../recipeapp/sensitive.json")
        key = path['path']   
        shutil.rmtree(f"{key}")
    else:
        pass
    ingredients = Ingredients.objects.all()
    ingredients.delete()
    return redirect("/images")

def get_keys(path):
    with open(path) as f:
        return json.load(f)

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