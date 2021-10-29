from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=254)
    slug = models.SlugField()
    intro = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True) # noqa
    image = models.ImageField(null=True, blank=True)
    body = models.TextField()
    body_sub_header = models.TextField(null=True, blank=True) # noqa
    body_text = models.TextField(null=True, blank=True) # noqa
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Change default order to decended date added"""
        ordering = ['-date_added']


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', null=True, blank=True, on_delete=models.SET_NULL) # noqa
    name = models.CharField(max_length=254)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Change default order to decended date added"""
        ordering = ['date_added']

    def __str__(self):
        return self.name
