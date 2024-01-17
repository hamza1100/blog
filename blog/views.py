from datetime import date
from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.

class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class AllPostsView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'all_posts'

# def posts(request):
#     try:
#         all_posts = Post.objects.all().order_by('-date')
#         return render(request, 'blog/all-posts.html', {
#             'all_posts': all_posts
#         })
#     except:
#         raise Http404()

class SinglePostView(DetailView):
    template_name = 'blog/post-detail.html'
    model = Post
    # context_object_name = 'post', 'post_tags'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.object.tag.all()
        return context


def post_detail(request, slug):
    try:
        # single_post = Post.objects.filter(slug=slug)
        single_post = Post.objects.get(slug=slug)
        return render(request, 'blog/post-detail.html', {
            'post': single_post,
            'post_tags': single_post.tag.all()
        })
    except:
        raise Http404()