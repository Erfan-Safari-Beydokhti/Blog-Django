from django.shortcuts import render
from django.views import View

def IndexView(request):
    return render(request, 'blog/index.html')
def PostsView(request):
    pass
def PostDetail(request, slug):
    pass