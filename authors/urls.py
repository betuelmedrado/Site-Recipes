


from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.register_views, name='register'),
    path('register/author', views.register_author, name='author')

]