from django.urls import path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings


app_name='recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipes, name="recipe"),
    path('recipes/category/<int:id>', views.category, name="category"),
    path('recipes/search/', views.search, name='search')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
