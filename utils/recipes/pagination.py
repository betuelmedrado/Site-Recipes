import math
from django.core.paginator import Paginator

def pagination_range(limite_pagina=list(range(1,20)), quant_pagina=4, current_pages=1):

    middle_range = math.ceil(quant_pagina/2)  # se o numero ficar quebrado, redonda para o maior 
    start_range = current_pages - middle_range
    last_range = current_pages + middle_range
    total_page = len(limite_pagina)
    

                        # "abs" é para tirar o sinal de "-" ou "+"
    start_range_offset = abs(start_range) if start_range < 0 else 0

    if start_range < 0:
        start_range = 0
        last_range = start_range_offset

    if last_range >= total_page:
        start_range -= abs(total_page - last_range)

    pagination = limite_pagina[start_range:last_range]    
    
    return {'pagination': pagination, 'limite_pagina': limite_pagina, 'quant_pagina':quant_pagina, 'current_pages': current_pages,
            'total_page': total_page,'start_range': start_range,'last_range':last_range, 'middle_range':middle_range,
            'first_page_out_of_range': current_pages > middle_range,
            'last_page_out_of_range': current_pages < total_page}



def make_pagination(request, obj_model, numero_na_pagina=4, per_pages=9):

    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1
    
    paginator = Paginator(obj_model, per_pages) # "4" ou "per_pages" é a quantidade de conteudo que a pagina vai mostrar 
    page_obj = paginator.get_page(current_page)        

    paginator_range = pagination_range(paginator.page_range, numero_na_pagina, current_page)

    return page_obj, paginator_range