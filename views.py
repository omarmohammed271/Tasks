from django.shortcuts import render,redirect
from .models import Blog

# Create your views here.
def blog(request):
    blogs = Blog.objects.all()

    if request.method =="POST":
        title = request.POST.get('title')
        owner = request.POST.get('author')
        post = request.POST.get('content')
        blog = Blog.objects.create(
            title=title,owner=owner,post=post
        )
        return redirect('blog:blog')


    context = {
        'blogs':blogs,
    }
    return render(request,'index.html',context) #response

# blog()