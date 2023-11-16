from rest_framework.response import Response
from collections import OrderedDict

from rest_framework import pagination

class UserPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        page_size_param = self.request.query_params.get('page_size', None)
        if page_size_param:
            ps = int(page_size_param)
        else:
            ps = self.page_size
        return Response(OrderedDict([
            ('page_size', ps),
            ('countItemsOnPage', len(data)),
            ('current', self.page.number),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('num_pages', self.page.paginator.num_pages),
            ('results', data),
        ]))
        