from django.shortcuts import render
from datetime import date

all_posts = [
    {
        'slug': 'learning-django',
        'title': 'django course',
        'author': 'Erfan Safari',
        'image': 'img.png',
        'date': date(2025, 6, 9),
        'short_description': 'This is Django Course for Beginner',
        'content': """
        Lorem ipsum dolor sit amet, consectet        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque enim itaque repellat! A aperiam
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque enim itaque repellat! A aperiam
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque enim itaque repellat! A aperiam
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque enim itaque repellat! A aperiam
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque enim itaque repellat! A aperiam
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque enim itaque repellat! A aperiam
        ur adipisicing elit. Cumque enim itaque repellat! A aperiam
        """
    },
    {
        'slug': 'learning-python',
        'title': 'python course',
        'author': 'Erfan Safari',
        'image': 'img_1.png',
        'date': date(2025, 6, 11),
        'short_description': 'This is Python Course for Beginner',
        'content': """
        Lorem ipsum dolor sit amet, consectetur         Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque enim itaque repellat! A aperiam
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque enim itaque repellat! A aperiam
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque enim itaque repellat! A aperiam
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque enim itaque repellat! A aperiam
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque enim itaque repellat! A aperiam
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque enim itaque repellat! A aperiam
        adipisicing elit. Cumque enim itaque repellat! A aperiam
        """
    },
    {
        'slug': 'learning-MySQL',
        'title': 'MySQL course',
        'author': 'Erfan Safari',
        'image': 'img_2.png',
        'date': date(2025, 6, 22),
        'short_description': 'This is MySQL Course for Beginner',
        'content': """
        Lorem ipsum dolor sit amet,         Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque enim itaque repellat! A aperiam
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque enim itaque repellat! A aperiam
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque enim itaque repellat! A aperiam
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque enim itaque repellat! A aperiam
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque enim itaque repellat! A aperiam
        consectetur adipisicing elit. Cumque enim itaque repellat! A aperiam
        """
    },

]


def get_date(post):
    return post['date']


def IndexView(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-2:]
    return render(request, 'blog/index.html', {'latest_posts': latest_posts})


def PostsView(request):
    return render(request, 'blog/all_post.html', {'all_posts': all_posts})


def PostDetail(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {'post': post})
