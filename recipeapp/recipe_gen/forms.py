from django import forms
from .models import *
 
 
class ImageForm(forms.ModelForm):
 
    class Meta:
        model = ingredient_images
        fields = ['ingredient_image']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ["ingredient_name"]

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ["is_saved"]

class MetricForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ['recipe_rating', 'recipe_review']
