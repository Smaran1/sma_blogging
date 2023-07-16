from rest_framework.pagination import PageNumberPagination

class MyPaginateNumber(PageNumberPagination):
    page_size = 6