


from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.register_views, name='register'),
    path('register/author', views.register_author, name='author'),
    path('register/login', views.login_user, name='login'),
    path('register/create',views.create_login, name='create_login'),
    path('register_recipes/', views.register_recipes, name='register_recipes'),
    path('save_recipes/', views.save_recipes, name='save_recipes'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/dashboard_edit/<int:id>', views.dashboard_recipe_edit, name='dashboard_edit')

] 