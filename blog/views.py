from django.shortcuts import render


def blog(request):
    """A view to return the blog page"""

    return render(request, 'blog/blog.html')
