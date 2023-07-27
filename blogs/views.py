from django.shortcuts import HttpResponse

import os
from mysite import settings
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blogs.serializer import PostSerializer
from blogs.models import Post
from rest_framework.generics import ListAPIView
from django.http import JsonResponse
from django.db.models import Q

def save_data(request): 

    p = Post(author = "Sma", title = 'PostgreSQL Architecture', text = 'I am smaran the great', comments = "So nice")
    p.save()
    return HttpResponse("OKAY") 

def del_data(request):
    d = Post.objects.filter(author='Smari').delete()
    return HttpResponse()


@api_view(['GET'])
def get_all_posts(request):
    post=Post.objects.order_by('-created_date')
    print(post)
    serializer= PostSerializer(post, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postBlog(request):
    serializer = PostSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    

@api_view(['GET'])
def paginating(request, page_number):
    per_page = 10
    posts = Post.objects.all()[page_number*per_page : ((page_number*per_page)+per_page)]
    serializer= PostSerializer(posts, many = True)
    print(serializer)
    return Response(serializer.data)    


@api_view(['GET'])
def paginating_offset(request, limit, offset_row):
    # limit = 10
    # offset_row = 7
    posts = Post.objects.all()[offset_row:(offset_row+limit)]
    serializer= PostSerializer(posts, many = True)
    print(serializer)
    return Response(serializer.data)    


# def pagination_search(request, search):
#     # if request.method == 'GET':
#         posts = Post.objects.all()
       
        
#         l = []
#         for post in posts:
#             if search in post.title:
#                 search_post = post.title
#                 l.append(search_post)
#                 print(l)


#         return JsonResponse(l)    

    # {jtu:80}
    # str = "{"+"key"+":"+"value"+"}"

# def pagination_search(request, search):
#         posts = Post.objects.filter(title__icontains = search)
        
#         titles = []
#         for post in posts:
#             title = post.title
#             titles.append(title)
#         print(titles)
#         return JsonResponse(titles, safe = False)    


def pagination_search(request, search, page_number, page_size):
        posts = Post.objects.filter(title__icontains = search)
        post_pag = posts[page_number*page_size:page_number*page_size+page_number]
        print(post_pag)    
        titles = post_pag.values_list('title', flat=True)
        print(titles)
        return JsonResponse(list(titles), safe = False)


class global_pag():
    page_number = 2
    page_size = 3

    
    def __init__(self, page_number, page_size):     
        self.page_number = page_number
        self.page_size = page_size 
        
        # return JsonResponse(list(data), safe = False )
    

    def all(self):
        data = Post.objects.all()[self.page_number*self.page_size:self.page_number*self.page_size+self.page_number]  
        l_data = list(data)
        return l_data

    def searched(self, search):
        data = Post.objects.filter(Q(title__icontains = search) | Q(author__icontains = search) |  Q(text__icontains = search))
        print(data)
        p_data = data[self.page_number*self.page_size:self.page_number*self.page_size+self.page_number]
        l_data = list(p_data)
        return l_data


@api_view(['GET'])
def get_all_posts_pag(request):
    sd = global_pag(2,3)
    post = sd.all()
    l = []
    for p in post:
        title = p.title
        author = p.author
        text = p.text
        created_date = p.created_date
        published_date = p.published_date
        data = [title, author, text, created_date, published_date]
        l.append(data)
    print(l)
    return JsonResponse(l, safe = False)




@api_view(['GET'])
def get_searched_posts_pag(request, search):
    sd = global_pag(2,3)
    s_post = sd.searched(search)
    l = []
    for p in s_post:
        title = p.title
        author = p.author
        text = p.text
        created_date = p.created_date
        published_date = p.published_date
        data = [title, author, text, created_date, published_date]
        l.append(data)
    print(l)
    return JsonResponse(l, safe = False)




