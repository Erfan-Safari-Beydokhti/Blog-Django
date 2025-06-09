from django.shortcuts import render
from django.views import View

def IndexView(request):
    return render(request, 'blog/index.html')
def PostsView(request):
    return render(request,'blog/all_post.html')
def PostDetail(request, slug):
    return render(request,'blog/post-detail.html')