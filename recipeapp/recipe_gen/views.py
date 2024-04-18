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

def index(request, user_id):
    """View function that will display the homepage of the web application. It will generate the forms for user to upload images, and to manually ad ingredients"""
    # Form for image uploads
    if request.method == 'POST' and "image" in request.POST:
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f"/index/"+str(user_id))
    else:
        form = ImageForm()

    # Form for manually adding ingredients
    if request.method == 'POST' and "manual" in request.POST:
        form2 = IngredientForm(request.POST)
        if form2.is_valid():
            ingredient = form2.save(commit=False)
            ingredient.save()
            form2 = IngredientForm()
    else:
        form2 = IngredientForm()
    instance = []
    saved_recs = Recipe_History.objects.filter(user_id=user_id)
    for i in saved_recs:
        instance.append(i)
    if instance == []:
        flag = None
    else:
        flag = 1
    ingredients = Ingredients.objects.all()
    context = {
        'user_id': user_id,
        'flag':flag,
        'form': form,
        'form2':form2,
        'ingredients':ingredients
    }
    return render(request, 'index.html', context)

def images(request, user_id):
    """View function for the page where user can choose which image to analyze from the images he has uploaded"""
    image = ingredient_images.objects.all()
    urls = []

    # Loop will unpackage image into lists within a list, for easier unpacking with django in the template
    for i in image:
        urls.append([i.id, i.ingredient_image.url])
    context = { 
        'user_id':user_id,
        'image': image,
        'urls': urls
        }
    return render(request, 'image.html', context)

def results(request, id, user_id):
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
        'user_id':user_id,
        'results':results,
        'path': path,
        'id': id
    }
    
    return render(request, 'results.html', context)

def add_remove_ingredients(request, user_id):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.save()
            form = IngredientForm
    else:
        form = IngredientForm
    ingredients = Ingredients.objects.all()
    context = {
        'user_id':user_id,
        'form' : form,
        'ingredients': ingredients,
    }
    return render(request, 'add_remove_ing.html', context)

"""End of object detection views"""


"""From here this deals with recipe saving and stuff related to the LLM"""

def llm_results(request, user_id):
    ingredients = Ingredients.objects.all()
    ings = []
    for i in ingredients:
        ings.append(i.ingredient_name)
    # recipe = LLM.generate_recipe(ings)
    # formatted_recipe = linebreaksbr(recipe)
    formatted_recipe = "test2"
    print(formatted_recipe)
    saved_rec = Recipe()
    saved_rec.recipe_content = formatted_recipe
    saved_rec.save()
    context = {
        'user_id':user_id,
        'recipe': formatted_recipe,
        'saved_rec': saved_rec
    }
    return render(request, 'llm_result.html', context)

def bool_change(request, id, user_id):
    recipe = Recipe.objects.get(recipe_id=id)
    recipe.is_saved = True
    recipe.save()
    save_instance = Recipe_History()
    save_instance.user_id = user_id
    save_instance.recipe_id = id
    save_instance.save()
    return redirect(f"/back/"+str(user_id))

def saved_recipes(request, user_id):
    saved_recs = []
    saved_rec_id = Recipe_History.objects.filter(user_id=user_id)
    for saved in saved_rec_id:
        recs = Recipe.objects.all().filter(recipe_id=saved.recipe_id)
        saved_recs.append(recs)
    print(saved_recs)
    context = {
        'user_id': user_id,
        'saved_recs' : saved_recs
    }
    return render(request, 'saved_recipes.html', context)

def recipe_page(request, id, user_id):
    flag = True
    recipe = Recipe.objects.get(recipe_id=id)
    history = Recipe_History.objects.all().filter(user_id=user_id)
    for h in history:
        if h.recipe_id == id:
            flag = False
        else:
            flag = True
    if request.method == 'POST':
        form = MetricForm(request.POST, instance=recipe)
        if form.is_valid():
            metric = form.save(commit=False)
            metric.save()
            form = MetricForm()
    else:
        form = MetricForm()
    context = {
        'user_id':user_id,
        'recipe': recipe,
        'form' : form,
        'flag':flag
    }
    return render(request, 'recipe.html', context)

def global_recipe(request, user_id):
    recipes = []
    recipe = Recipe.objects.all()
    for i in recipe:
        recipes.append(i)
    print(recipes)
    context={
        'user_id': user_id,
        'recipes':recipes
    }
    return render(request, 'global_recipe.html', context)

"""LLM and recipe stuff ends here"""

"""User Login and Registration functions"""

def registration(request):
    user_data = Users.objects.all()
    message=""
    usernames = []
    for u in user_data:
        usernames.append(u.username)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        username = request.POST["username"]
        if form.is_valid() and username not in usernames:
            register = form.save(commit=False)
            register.save()
            return redirect('/')
        else:
            message = "Username already exists"
    else:
        form=RegisterForm()
    context = {
        'message':message,
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

def delete_image(request, id, user_id):
    images = ingredient_images.objects.get(id=id)
    os.remove(f".{images.ingredient_image.url}")
    images.delete()
    return redirect(f"/index/"+str(user_id))

def delete_saved_recipe(request, id, user_id):
    history = Recipe_History.objects.get(recipe_id=id, user_id=user_id)
    history.delete()
    recipe = Recipe.objects.get(recipe_id=id)
    recipe.delete()
    return redirect(f"/index/"+str(user_id))

def del_back_ing(request, user_id):
    path = f"{os.getcwd()}\\recipe_gen\\static\\output_images"
    if os.path.isdir(path):  
        shutil.rmtree(f"{path}")
    else:
        pass
    ingredients = Ingredients.objects.all()
    ingredients.delete()
    return redirect(f"/images/"+str(user_id))

def back(request, user_id):
    path = f"{os.getcwd()}\\recipe_gen\\static\\output_images"
    if os.path.isdir(path):  
        shutil.rmtree(f"{path}")
    else:
        pass
    ingredients = Ingredients.objects.all()
    ingredients.delete()
    return redirect(f"/index/"+str(user_id))

def del_back(request, user_id):
    path = f"{os.getcwd()}\\recipe_gen\\static\\output_images"
    if os.path.isdir(path):  
        shutil.rmtree(f"{path}")
    else:
        pass
    ingredients = Ingredients.objects.all()
    ingredients.delete()
    return redirect(f"/images/"+str(user_id))

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