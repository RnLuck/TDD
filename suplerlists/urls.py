"""suplerlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path,re_path,include
from django.conf.urls import url
from lists import views as list_views
from lists import urls as list_urls

# urlpatterns = [
#     path('', views.home_page,name='home'),
#     path('lists/new',views.new_list,name='new_list'),
#     re_path(r'^lists/(.+)/$',views.view_list,name='view_list'),
#     re_path(r'^llists/(\d)/$',views.view_list,name='view_list'),
# ]

urlpatterns = [
    path('',list_views.home_page,name='home'),
    re_path(r'^lists/',include(list_urls)),
]

