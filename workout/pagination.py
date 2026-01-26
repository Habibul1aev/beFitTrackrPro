from rest_framework import pagination

class WorkoutPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'pagesize'
    page_query_param = 'page'
    max_page_size = 100
