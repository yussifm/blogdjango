
from django.shortcuts import render, redirect
from .models import Posts
from datetime import datetime

# Create your views here.
def index(request):
    all_posts = Posts.objects.all()
    return render(request, 'posts/index.html', context={'posts': all_posts})

def addPost(request):
    if request.method == 'POST':
        blog_title = request.POST['title']
        descriptoin = request.POST['decs']
        if(blog_title !="" and descriptoin != ''):
            blog = Posts(title = blog_title,decs=descriptoin, date_of_post = datetime.now())
            blog.save()
            return redirect(to='index.html')
        else:
              return render(request=request,template_name='posts/addpost.html',)
            
    return render(request=request,template_name='posts/addpost.html',)

def detailPost(request, pk):
    post = Posts.objects.get(id=pk)
    return render(request, 'posts/details.html', context={'post': post})