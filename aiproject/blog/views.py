from django.shortcuts import render
from django.http import Http404

# Create your views here.

from .models import Post 

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.xhtml', {'posts': posts})

def post_detail(request, id):
    # try:
    #     post = Post.published.get(id = id)
    # except Post.DoesNotExist:
    #     raise Http404("No Post found.")
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.xhtml' {'post': post})