from django.shortcuts import render
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "blog/index.html", context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post": post})
