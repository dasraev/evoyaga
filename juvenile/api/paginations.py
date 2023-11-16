from rest_framework.response import Response
from collections import OrderedDict

from rest_framework import pagination

class JuvenilePagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response(OrderedDict([
             ('countItemsOnPage', len(data)),
             ('current', self.page.number),
             ('next', self.get_next_link()),
             ('previous', self.get_previous_link()),
             ('num_pages', self.page.paginator.num_pages),
             ('results', data),
         ]))
