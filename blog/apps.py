"""import AppConfig"""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Create class"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
