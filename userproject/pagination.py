from rest_framework.pagination import PageNumberPagination
from rest_framework import pagination
from rest_framework.response import Response
from django.core.paginator import Paginator
from collections import OrderedDict

class CustomPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1
    page_query_param = 'p'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })