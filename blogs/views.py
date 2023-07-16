from django.shortcuts import HttpResponse
import os
from mysite import settings
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PostSerializer
from .models import Post




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