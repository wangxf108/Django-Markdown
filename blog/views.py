from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts':posts})


def detail(request, pk):
    # add first(),then in the template you can get the data. or nothing there.
    post = Post.objects.filter(pk=pk).first()
    # content = post.body

    return render(request, 'blog/detail.html', {'post':post})