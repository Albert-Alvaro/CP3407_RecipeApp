from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
    
class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True, null=False)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20, default='000')

class Recipe(models.Model):
    recipe_id = models.BigAutoField(primary_key=True)
    recipe_content = models.TextField(null=True)
    recipe_steps = models.CharField(max_length=40000)
    recipe_rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], null=True)
    recipe_review = models.TextField(null=True)
    recipe_category = models.CharField(max_length=45)
    is_saved = models.BooleanField(default=False)

class Ingredients(models.Model):
    ingredient_id = models.BigAutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=60, null=True)
    ingredient_type = models.CharField(max_length=60, null=True)

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


