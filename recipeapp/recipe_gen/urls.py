from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('index/<int:id>', views.index, name = "index"),
    path('images/<int:id>',views.images, name = "images"),
    path('results/<int:id>/<int:id2>', views.results, name='results'),
    path('delete-images/<int:id>',views.delete_image,name="delete-images"),
    path('back/<int:id>', views.back, name='back'),
    path('del-back/<int:id>', views.del_back, name='del_back'),
    path('add_remove_ing/<int:id>/<int:id2>', views.add_remove_ingredients, name='add_remove_ing'),
    path('del-back-ing', views.del_back_ing, name="del_back_ing"),
    path('llm-result/<int:id>', views.llm_results, name='llm_result'),
    path('saved_recipes', views.saved_recipes, name='saved_recipes'),
    path('bool-change/<int:id>', views.bool_change, name='bool-change'),
    path('del-saved-rec/<int:id>', views.delete_saved_recipe, name='del-saved-rec'),
    path('recipe_page/<int:id>', views.recipe_page, name='recipe_page'),
    path('register', views.registration, name='register'),
    path('', views.login, name='login') 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)