from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .yolo import *
import shutil
import json
from .llm import LLM
from django.template.defaultfilters import linebreaksbr
# Create your views here.

"""Object Detection Views"""

def index(request, id):
    if request.method == 'POST' and "image" in request.POST:
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f"/index/"+str(id))
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
        'id': id,
        'form': form,
        'form2':form2,
        'ingredients':ingredients
    }
    return render(request, 'index.html', context)

def images(request, id):
    image = ingredient_images.objects.all()
    urls = []
    for i in image:
        urls.append([i.id, i.ingredient_image.url])
    context = { 
        'id':id,
        'image': image,
        'urls': urls
        }
    return render(request, 'image.html', context)

def results(request, id, id2):
    image = ingredient_images.objects.get(id=id)
    path = image.ingredient_image.url
    items, file = OBJ_DET.detect(path, id)
    results = numerated_results(items)
    path = f"/output_images/{id}/{file}"
    print(path)

    for ing in results:
        ingredients = Ingredients()
        ingredients.ingredient_name = ing[0]
        ingredients.save()
    context = {
        'id2':id2,
        'results':results,
        'path': path,
        'id': id
    }
    
    return render(request, 'results.html', context)

def add_remove_ingredients(request, id, id2):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.save()
    else:
        form = IngredientForm
    ingredients = Ingredients.objects.all()
    context = {
        'id2':id2,
        'form' : form,
        'ingredients': ingredients,
        'id': id
    }
    return render(request, 'add_remove_ing.html', context)

def navbar(id):
    return {'id':id}

"""End of object detection views"""


"""From here this deals with recipe saving and stuff related to the LLM"""

def llm_results(request, id):
    ingredients = Ingredients.objects.all()
    print(id)
    ings = []
    for i in ingredients:
        ings.append(i.ingredient_name)
    # recipe = LLM.generate_recipe(ings)
    # formatted_recipe = linebreaksbr(recipe)
    formatted_recipe = "test"
    print(formatted_recipe)
    saved_rec = Recipe()
    saved_rec.recipe_content = formatted_recipe
    saved_rec.save()
    context = {
        'recipe': formatted_recipe,
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
        if r.is_saved == False:
            r.delete()
    saved_recs = Recipe.objects.all()
    context = {
        'saved_recs' : saved_recs
    }
    return render(request, 'saved_recipes.html', context)

def recipe_page(request, id):
    recipe = Recipe.objects.get(recipe_id=id)
    if request.method == 'POST':
        form = MetricForm(request.POST, instance=recipe)
        if form.is_valid():
            metric = form.save(commit=False)
            metric.save()
    else:
        form = MetricForm()
    context = {
        'recipe': recipe,
        'form' : form,
    }
    return render(request, 'recipe.html', context)

"""LLM and recipe stuff ends here"""

"""User Login and Registration functions"""

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            register = form.save(commit=False)
            print(register)
            register.save()
            return redirect('/')
    else:
        form=RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)



def login(request):
    user_data = Users.objects.all()
    username=""
    password=""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
    if username != None and password !=None:
        for user in user_data:
            print(user.username, user.password)
            if user.username == username and user.password == password:
                return redirect(f"/index/"+str(user.user_id))
            else:
                continue
    else:
        pass
    context={
    }
    return render(request, 'login.html', context)


"""Back and delete functions for general navigation"""

def delete_image(request, id):
    images = ingredient_images.objects.get(id=id)
    os.remove(f".{images.ingredient_image.url}")
    images.delete()
    return redirect("/index")

def delete_saved_recipe(request, id):
    recipe = Recipe.objects.get(recipe_id=id)
    recipe.delete()
    return redirect('/saved_recipes')

def del_back_ing(request):
    path = get_keys("../recipeapp/sensitive.json")
    key = path['path']
    if os.path.isdir(key):  
        shutil.rmtree(f"{key}")
    else:
        pass
    ingredients = Ingredients.objects.all()
    ingredients.delete()
    return redirect(f"/images")

def back(request, id):
    path = get_keys("../recipeapp/sensitive.json")
    key = path['path']
    if os.path.isdir(key):  
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
    return redirect(f"/index/"+str(id))

def del_back(request, id):
    path = get_keys("../recipeapp/sensitive.json")
    key = path['path']
    if os.path.isdir(key):  
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