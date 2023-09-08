from django.shortcuts import HttpResponse 

from django.http import JsonResponse  , request

from .models import Post


from mysite.helpers.global_pagination import GlobalPagination


class AllPost(GlobalPagination):
    query_set = Post.objects.all()


