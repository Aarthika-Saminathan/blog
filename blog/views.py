from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
import logging

posts = [
    {'id': 1, 'title': 'post1', 'content': 'content of post1'},
    {'id': 2, 'title': 'post2', 'content': 'content of post2'},
    {'id': 3, 'title': 'post3', 'content': 'content of post3'},
    {'id': 4, 'title': 'post4', 'content': 'content of post4'},
]

def index(request):
    blog_title = "Latest posts"
    return render(request, 'blog/index.html', {'blog_title': blog_title, 'posts': posts})

def detail(request, post_id):
    post = next((item for item in posts if item['id'] == int(post_id)), None)
    
    if post is None:
        return HttpResponse("Post not found", status=404)

    logger = logging.getLogger("testing")
    logger.debug(f"post variable is {post}")

    return render(request, 'blog/detail.html', {'post': post})

def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))

def new_url_view(request):
    return HttpResponse("This is the new URL")
