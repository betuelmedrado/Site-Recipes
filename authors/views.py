from django.shortcuts import render, redirect
from .forms import RegisterForms

from django.http import Http404



# Create your views here.

def register_views(request):
    
    # === A session do usuario logado ===
    # request.session['namber'] = request.session.get('namber') or 1
    # request.session['namber'] += 1
    # ==================              

    register_form_data = request.session.get('register_form_data', None)

    forms = RegisterForms(register_form_data)
    
    return render(request, 'pages/register_view.html', context={'forms':forms})


def register_author(request):    

    if not request.POST:
        raise Http404()

    post = request.POST
    request.session['register_form_data'] = post
    forms = RegisterForms(post)    

    return redirect('authors:register')
