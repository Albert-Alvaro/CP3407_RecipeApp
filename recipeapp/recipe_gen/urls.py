from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('images',views.images, name = "images"),
    path('results/<int:id>', views.results, name='results'),
    path('delete-images',views.delete_image,name="delete-images"),
    path('back', views.back, name='back'),
    path('del-back/<int:id>', views.del_back, name='del_back'),
    path('add_remove_ing', views.add_remove_ingredients, name='add_remove_ing'),
    path('del-back-ing', views.del_back_ing, name="del_back_ing")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)