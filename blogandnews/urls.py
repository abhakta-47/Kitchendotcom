from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogandnews, name="blogandnews"),
    path('blog/<int:blogId>', views.blog, name="blog"),
    path('news/<int:newsId>', views.news, name="news"),

]