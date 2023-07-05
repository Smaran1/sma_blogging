from django.shortcuts import HttpResponse
from blogs.models import Post
# Create your views here.
def save_data(request):   
    p = Post(author = "Sma", title = 'PostgreSQL Architecture', text = 'I am smaran the great', comments = "So nice")
    p.save()
    return HttpResponse() #k grxa why need this?

def del_data(request):
    d = Post.objects.filter(author='Smari').delete()
    return HttpResponse()