from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .yolo import *
import shutil
import json
from .llm import LLM
# Create your views here.

"""Object Detection Views"""

def index(request):
    if request.method == 'POST' and "image" in request.POST:
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ImageForm()
    if request.method == 'POST' and "manual" in request.POST:
        form2 = IngredientForm(request.POST)
        if form2.is_valid():
            ingredient = form2.save(commit=False)
            ingredient.save()
    else:
        form2 = IngredientForm()
    ingredients = Ingredients.objects.all()
    context = {
        'form': form,
        'form2':form2,
        'ingredients':ingredients
    }
    return render(request, 'index.html', context)

def images(request):
    image = ingredient_images.objects.all()
    urls = []
    for i in image:
        urls.append([i.id, i.ingredient_image.url])
    context = { 
        'image': image,
        'urls': urls
        }
    return render(request, 'image.html', context)

def results(request, id):
    image = ingredient_images.objects.get(id=id)
    path = image.ingredient_image.url
    items, file = OBJ_DET.detect(path, id)
    results = numerated_results(items)
    path = f"/output_images/{id}/{file}"

    for ing in results:
        ingredients = Ingredients()
        ingredients.ingredient_name = ing[0]
        ingredients.save()
    context = {
        'results':results,
        'path': path,
        'id': id
    }
    
    return render(request, 'results.html', context)

def add_remove_ingredients(request, id):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.save()
    else:
        form = IngredientForm
    ingredients = Ingredients.objects.all()
    context = {
        'form' : form,
        'ingredients': ingredients,
        'id': id
    }
    return render(request, 'add_remove_ing.html', context)

"""End of object detection views"""


"""From here this deals with recipe saving and stuff related to the LLM"""

def llm_results(request):
    ingredients = Ingredients.objects.all()
    ings = []
    for i in ingredients:
        ings.append(i.ingredient_name)
    recipe = LLM.generate_recipe(ings)
    saved_rec = Recipe()
    saved_rec.recipe_content = recipe
    saved_rec.save()
    context = {
        'recipe': recipe,
        'saved_rec': saved_rec
    }
    return render(request, 'llm_result.html', context)

def bool_change(request, id):
    recipe = Recipe.objects.get(recipe_id=id)
    recipe.is_saved = True
    recipe.save()
    return redirect('/back')

def saved_recipes(request):
    recipes = Recipe.objects.all()
    for r in recipes:
        print(r)
        if r.is_saved == False:
            r.delete()
    saved_recs = Recipe.objects.all()
    context = {
        'saved_recs' : saved_recs
    }
    return render(request, 'saved_recipes.html', context)

"""LLM and recipe stuff ends here"""

"""Back and delete functions for general navigation"""

def delete_image(request, id):
    images = ingredient_images.objects.get(id=id)
    os.remove(f".{images.ingredient_image.url}")
    images.delete()
    return redirect("/")

def delete_saved_recipe(request, id):
    recipe = Recipe.objects.get(recipe_id=id)
    recipe.delete()
    return redirect('/saved_recipes')

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
    recipe = Recipe.objects.all()
    for r in recipe:
        if r.is_saved == True:
            continue
        else:
            r.delete()
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

"""End of back and delete functions"""

"""Start of Miscalleneous functions"""

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

"""End of Miscalleneous functions"""