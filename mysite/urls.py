"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogs.views import *
from blogs import views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('blog/del/', del_data),
    path('blog/save/', save_data),
    path('blog/all/', get_all_posts),
    path('blog/post/', postBlog),
    # path('blog/list/', views.BlogList.as_view()),
    path('page/<int:page_number>/', paginating),
    path('page/<int:limit>/<int:offset_row>/', paginating_offset),
    path('page/<str:search>/<int:page_number>/<int:page_size>/', pagination_search ),
    path('gpage/<int:page_number>/<int:page_size>/', get_all_posts_pag ),
    path('gpage/<str:search>/<int:page_number>/<int:page_size>/', get_searched_posts_pag)
    # path('blog/post/<int:page_number>/', views.paginating, name='paginating'),
]

