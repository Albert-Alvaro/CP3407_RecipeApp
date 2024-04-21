from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('index/<int:user_id>', views.index, name = "index"),
    path('images/<int:user_id>',views.images, name = "images"),
    path('results/<int:id>/<int:user_id>', views.results, name='results'),
    path('delete-images/<int:id>/<int:user_id>',views.delete_image,name="delete-images"),
    path('back/<int:user_id>', views.back, name='back'),
    path('del-back/<int:user_id>', views.del_back, name='del_back'),
    path('add_remove_ing/<int:user_id>', views.add_remove_ingredients, name='add_remove_ing'),
    path('del-back-ing/<int:user_id>', views.del_back_ing, name="del_back_ing"),
    path('llm-result/<int:user_id>', views.llm_results, name='llm_result'),
    path('saved_recipes/<int:user_id>', views.saved_recipes, name='saved_recipes'),
    path('bool-change/<int:id>/<int:user_id>', views.bool_change, name='bool-change'),
    path('del-saved-rec/<int:id>/<int:user_id>', views.delete_saved_recipe, name='del-saved-rec'),
    path('recipe_page/<int:id>/<int:user_id>', views.recipe_page, name='recipe_page'),
    path('register', views.registration, name='register'),
    path('global/<int:user_id>', views.global_recipe, name='global'),
    path('delete_ingredient/<int:user_id>/<int:ing_id>', views.delete_ingredient, name='delete_ingredient'),
    path('delete_ingredient_index/<int:user_id>/<int:ing_id>', views.delete_ingredient_index, name='delete_ingredient_index'),
    path('', views.login, name='login') 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)