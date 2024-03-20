from django import forms
from .models import *
 
 
class ImageForm(forms.ModelForm):
 
    class Meta:
        model = ingredient_images
        fields = ['ingredient_image']

class OutputForm(forms.ModelForm):
    
    class Meta:
        model = result_images
        fields = ['url']