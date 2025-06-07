from django.urls import path
from .views import IndexView,PostsView,PostDetail
urlpatterns=[
    path('',IndexView,name='index'),
    path('posts/',PostsView,name='posts'),
    path('posts/<slug:slug>',PostDetail,name='post'),
]