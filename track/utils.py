from django.core.paginator import Paginator
def api_paginator(queryset, query_params):
    page_size = query_params.get('limit',10)
    page_number = query_params.get('page',1)
    return Paginator(queryset, page_size).page(page_number)