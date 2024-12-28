from django.urls import path
from . import views

urlpatterns = [
    path('',views.posts_lest, name="posts"),
    path('<slug:slug>',views.post_page, name="post_page"),
]