from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

url_patterns = [
    path('', views.index, name = "index")
]