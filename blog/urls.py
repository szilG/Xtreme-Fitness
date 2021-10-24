from django.contrib import admin

from django.urls import path
from . import views
admin.autodiscover()


urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', views.blog_details, name='blog_details'),
]
