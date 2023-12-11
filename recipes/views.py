from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from utils.recipes.factory import make_recipe
from django.http import Http404

from django.core.paginator import Paginator # Para paginação de pagina

from .models import Recipes, Category

from django.db.models import Q  # Só para dizer para o banco de dados "OR"

from utils.recipes.pagination import pagination_range, make_pagination

from django.contrib import messages

import os 

# Minha Variavel PER_PAGE 
PER_PAGES = int(os.environ.get('PER_PAGE', 4)) # "PER_PAGE" Está no arquivo que criei ".env" e só retorna 'strings'

# Create your views here.
def home(request):

    recipes = Recipes.objects.filter(is_plubeshed=True).order_by('-id')

    # Fazendo a paginação da view "AULA 117 SECÃO 11"
    # 
    page_obj, paginator_range = make_pagination(request, recipes, 4, PER_PAGES)

    # Messages of error
    messages.success(request, 'Deu tudo certo por aqui')
    messages.error(request, 'Deu tudo certo por aqui')
    messages.warning(request, 'Deu tudo certo por aqui')

    #return render(request, 'recipes/pages/home.html', context={"recipes":[make_recipe() for _ in range(10)]})
    return render(request, 'recipes/pages/home.html', context={"recipes": page_obj, 'page_range':paginator_range})



def recipes(request, id):
    #model = Recipes.objects.get(id=id, is_plubeshed=True)
        
    #return render(request, 'recipes/pages/recipes_views.html', context={"recipe":make_recipe(), 
     #                                                                   "is_detail_page":True})
    model = get_object_or_404(Recipes, id=id, is_plubeshed=True)

    return render(request, 'recipes/pages/recipes_views.html', context={'recipe':model,"is_detail_page":True})


def category(request, id):
    
    # "AULA 63" - "get_list_or_404" é para quando não estiver uma categoria para não dar erro 
    recipes = get_list_or_404(Recipes.objects.filter(category__id=id, is_plubeshed=True))

    # category retorna uma 'query set' uma lista e pegamos o primeiro objeto com first() e ou last()
    #return render(request, 'recipes/pages/category.html', context={'recipes': recipes, 'category': f"{recipes.first().category.name} - Category"})
    return render(request, 'recipes/pages/category.html', context={'recipes': recipes, 'category': f"{recipes[0].category.name} - Category"})


def search(request):

    if not request.GET.get('entrada'):
        raise Http404('Nada para ser')

    get_entrada = request.GET.get('entrada', '').strip()

    # "icontains" é para saber se tem o texto digitádo no banco de dados ingnorando se é letra maiuscula ou minuscula
    # "contains" é para saber se tem o texto digitádo no banco de dados
    categoria  = Recipes.objects.filter(Q(title__icontains=get_entrada) | Q(description__icontains=get_entrada),)

    categoria = categoria.filter(is_plubeshed=True)


    obj_page, page_range = make_pagination(request, categoria, 4, PER_PAGES)
    

    return render(request, 'recipes/pages/search.html', context={'recipes': obj_page, 
                                                                 'get_entrada':get_entrada, 
                                                                 'page_range':page_range,
                                                                 'additional_url':f'&entrada={get_entrada}'})