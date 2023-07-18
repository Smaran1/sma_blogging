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

#Creating global pagination
# class BlogList(ListAPIView):
#     post = Post.objects.all()
#     serializer = PostSerializer
   

# Create your views here.

def save_data(request): 

    p = Post(author = "Sma", title = 'PostgreSQL Architecture', text = 'I am smaran the great', comments = "So nice")
    p.save()
    return HttpResponse("OKAY") 

def del_data(request):
    d = Post.objects.filter(author='Smari').delete()
    return HttpResponse()

# def get_all_db(request):
#     db= Post.objects.all()
#     return HttpResponse()


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
    


def paginating(request, page_number):
    # total_records = Post.objects.count()
    per_page = 10
    # starting = 1
    posts = list(Post.objects.all())
    listing = posts[page_number*per_page : ((page_number*per_page)+per_page)]
    print(listing)
    # sliced = posts[starting:per_page]
    # print(sliced)
    serializer= PostSerializer(listing, many = True)
    print(serializer)
    return Response(serializer.data)    



# def paginating(request, page_number):
#     per_page = 10
#     starting = (page_number - 1) * per_page
#     ending = page_number * per_page

#     posts = list(Post.objects.all())
#     listing = posts[starting:ending]
    
#     serializer = PostSerializer(listing, many=True)
#     return Response(serializer.data)
    



# def paginating(request, pg_no):
#     total_records = Post.objects.count()
#     per_page = 10
#     start_index = (pg_no - 1) * per_page
#     end_index = pg_no * per_page

#     # Fetch all Post objects from the database and convert them to a list
#     posts = list(Post.objects.all())

#     # Slice the list to get the appropriate subset of posts for the given page
#     sliced_posts = posts[start_index:end_index]

#     # Serialize the sliced_posts list using PostSerializer
#     serializer = PostSerializer(sliced_posts, many=True)

#     # Return the serialized data as JSON response using DRF's Response class
#     return Response(serializer.data)


# @api_view(['GET'])
# def paginating(request, pg_no):
#     total_records = Post.objects.count()
#     per_page = 10
#     start_index = (pg_no - 1) * per_page
#     end_index = pg_no * per_page

#     # Fetch all Post objects from the database
#     posts = Post.objects.all()

#     # Slice the queryset to get the appropriate subset of posts for the given page
#     sliced_posts = posts[start_index:end_index]

#     # Serialize the sliced_posts queryset using PostSerializer
#     serializer = PostSerializer(sliced_posts, many=True)

#     # Return the serialized data as JSON response using DRF's Response class
#     return Response(serializer.data)