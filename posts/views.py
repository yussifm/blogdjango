from django.shortcuts import render
from .models import Posts

# Create your views here.
def index(request):
    all_posts = Posts.objects.all()
    return render(request, 'posts/index.html', context={'posts': all_posts})

def addPost(request):
    return render(request=request,template_name='posts/addpost.html',)

def detailPost(request, pk):
    post = Posts.objects.get(id=pk)
    return render(request, 'posts/details.html', context={'post': post})