from django.db import models

# Create your models here.

class Recipe(models.Model):
    recipe_id = models.BigAutoField(primary_key=True)
    recipe_content = models.CharField(max_length=5000)
    recipe_steps = models.CharField(max_length=4000)
    recipe_rating = models.IntegerField()
    recipe_category = models.CharField(max_length=45)
    is_saved = models.BooleanField(default=False)

class Ingredients(models.Model):
    ingredient_id = models.BigAutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=60, null=True)
    ingredient_type = models.CharField(max_length=60, null=True)

class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100, null=False)

class Prompts(models.Model):
    prompt_id = models.BigAutoField(primary_key=True)
    prompt_content = models.CharField(max_length=500)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

class Recipe_History(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)

class ingredient_images(models.Model):
    id = models.BigAutoField(primary_key=True)
    ingredient_image = models.ImageField(upload_to='images/')


