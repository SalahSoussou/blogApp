from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('',views.posts_lest, name="list"),
    path('<slug:slug>',views.post_page, name="post_page"),
]