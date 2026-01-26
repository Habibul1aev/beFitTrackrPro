from rest_framework import pagination

class AccountPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'pagesize'
    page_query_param = 'page'
    max_page_size = 100
