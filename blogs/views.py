from django.shortcuts import HttpResponse
from blogs.models import Post
# Create your views here.
def save_data(request):   
    p = Post(author = "Smari", title = 'PostgreSQL Architecture', text = 'I am smaran the great', comments = "So nice")
    p.save()
    return HttpResponse()