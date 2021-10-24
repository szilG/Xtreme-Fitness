from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CommentForm
from .models import Post


def blog(request):
    """A view to return the blog page"""

    posts = Post.objects.all()

    template = 'blog/blog.html'
    context = {
        'posts': posts,
    }

    return render(request, template, context)


def blog_details(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('blog_details', slug=post.slug)
    else:
        form = CommentForm()

    template = 'blog/blog_details.html'
    context = {
        'post': post,
        'form': form,
        'slug': post.slug,
    }

    return render(request, template, context)
