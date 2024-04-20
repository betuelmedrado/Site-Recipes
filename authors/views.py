
from django.shortcuts import render, redirect
from .forms import RegisterForms, Login, FormEditRecipes
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required # Para uma view restrita para o usuario poder sair
from django import forms

from django.http import Http404

from recipes.views import Recipes


# Create your views here.

def register_views(request):
    
    # === A session do usuario logado ===
    # request.session['namber'] = request.session.get('namber') or 1
    # request.session['namber'] += 1
    # ==================              

    register_form_data = request.session.get('register_form_data', None)    
    
    forms = RegisterForms(register_form_data)
    
    return render(request, 'pages/register_view.html', context={'forms':forms,
                                                                'forms_action':reverse('authors:author')})


def register_author(request):    

    if not request.POST:
        raise Http404()

    post = request.POST

    # Crei uma chave dentro da minha session chamada 'register_form_data'
    request.session['register_form_data'] = post
    forms = RegisterForms(post)    

    if forms.is_valid():

        # .save(commit=False) is to not save to the database but to the variable
        user = forms.save(commit=False)

        # cripting the password 
        user.set_password(user.password)
        
        # And saved in the database
        user.save()

        # messages of success in the template 
        messages.success(request,'User saved with success!')

        # if saved the user the delet the fields of forms
        del(request.session['register_form_data'])
    else:
        messages.error(request,'invalid save')

    return redirect('authors:login')


def login_user(request):

    session_login = request.session.get('session_login', None)

    form = Login(session_login)    

    return render(request, 'pages/login.html', context={'forms':form, 'forms_action': reverse('authors:create_login')})



def create_login(request):

    request.session['session_login'] = request.POST

    # valid the fields of forms
    forms = Login(request.POST)
    url_login = reverse('authors:dashboard')

    if forms.is_valid():

        authentica_user = authenticate(
            username = forms.cleaned_data.get('username'),
            password = forms.cleaned_data.get('password')
        )

        if authentica_user is not None:
            messages.success(request, 'You this is logaded whith ')
            
            # after of authenticated the user log he
            login(request, authentica_user) 
            try:
                del(request.session['session_login'])            
            except:
                pass
        else:
            messages.error(request,'invalid credential!')
    else:
        messages.error(request,'error to validad form data')

    
    return redirect(url_login)


def register_recipes(request): 

    post = request.session.get('forms_post', None)

    forms_register = FormEditRecipes(  
        data=post        

    )

    sorc = 'authors:save_recipes'
    return render(request, 'pages/register_recipes.html',context={'forms':forms_register, 'forms_action':reverse(sorc)})


def save_recipes(request):

    post = request.POST

    form_register = FormEditRecipes(
        data = request.POST or None,
        files = request.FILES 
    )

    request.session['forms_post'] = post


    if request.POST:
    
        if form_register.is_valid():            
            recipes: Recipes = form_register.save(commit=False)
            
            recipes.is_plubeshed = False
            recipes.author = request.user            
            recipes.save()

            messages.success(request,'Recipes save with success!')  
            del(request.session['forms_post'])      
            return redirect(reverse('authors:register_recipes'))
        

    return redirect(reverse('authors:register_recipes'))


# sessão 13 aula 159 Uderm 
@login_required(login_url='authors:login', redirect_field_name='next')
def logout_view(request):
    
    if not request.POST:        
        return redirect(reverse('authors:login'))

    if request.POST.get('input_name') != request.user.username:        
        return redirect(reverse('authors:login'))

    logout(request)
    return redirect(reverse('authors:login'))


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard(request):

    recipes = Recipes.objects.filter(
        is_plubeshed=False,
        author=request.user
    )

    return render(request, 'pages/dashboard.html',context={'recipes':recipes})


@login_required(login_url='author:login', redirect_field_name='next')
def dashboard_recipe_edit(request, id):

     recipes = Recipes.objects.filter(
        is_plubeshed=False,
        author=request.user,
        pk=id).first()

     if not recipes:
        return Http404()

     forms = FormEditRecipes(
        data=request.POST or None,
        files=request.FILES or None,          
        # a instance não aceita interavel então foi usado "first()" no recipes para vim somente um resultado
        instance=recipes
    )     

     if forms.is_valid():
                  
         recipes = forms.save(commit=False)
         
         recipes.preparation_steps_is_html = False
         recipes.is_plubeshed = False

         recipes.save()

         messages.success(request, 'Recipes saved with success!')
         
         return redirect(reverse('authors:dashboard_edit', args=(id,)))
    
     return render(request,'pages/dashboard_edit.html', context={'recipes':recipes, 'forms':forms})