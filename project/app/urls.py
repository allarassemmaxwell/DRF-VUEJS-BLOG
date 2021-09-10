from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('posts/', BlogList.as_view()),
    path('posts/detail/<slug:post_slug>', post_detail_view, name="post_detail"),
    path('posts/<slug:post_slug>', BlogDetail.as_view()),
]