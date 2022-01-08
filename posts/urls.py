from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.addPost, name='posts'),
    path('post/<str:pk>', views.detailPost, name="post")
]
