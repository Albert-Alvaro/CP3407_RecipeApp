from django.db import models

# Create your models here.

class Recipe(models.Model):
    recipe_id = models.BigAutoField(primary_key=True)
    recipe_content = models.CharField(max_length=5000, null=False)
    recipe_steps = models.CharField(max_length=4000, null=False)
    recipe_rating = models.IntegerField()
    recipe_category = models.CharField(max_length=45, null=False)

class Ingredients(models.Model):
    ingredient_id = models.BigAutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=60, null=False)
    ingredient_type = models.CharField(max_length=60, null=False)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)

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

