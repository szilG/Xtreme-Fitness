from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=254)
    slug = models.SlugField()
    intro = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Change default order to decended date added"""
        ordering = ['-date_added']
