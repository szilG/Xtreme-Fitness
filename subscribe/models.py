from django.db import models
from django.contrib.auth.models import User


class Subscribe(models.Model):
    """Make subscribe class with email and date field"""
    email = models.EmailField(max_length=254, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Add verbose meta"""
        verbose_name_plural = 'subscribers'

    def __str__(self):
        return self.email
