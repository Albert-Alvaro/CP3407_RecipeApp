from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Ingredients)
admin.site.register(models.Prompts)
admin.site.register(models.Recipe)
admin.site.register(models.Recipe_History)
admin.site.register(models.Users)