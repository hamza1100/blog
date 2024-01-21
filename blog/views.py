from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.conf import settings
from openai import OpenAI

client = OpenAI(api_key=settings.OPENAI_API_KEY)
from django.views.generic import ListView
from django.views import View
from .forms import CommentForm

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

class SinglePostView(View):

    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get('stored_posts')
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False

        return is_saved_for_later
    
    def generate_prompt_for_openai(self, input):
        prompt = """add a comment on the following text just like someone would do on social media, 
        sharing his/her experience. length should be within 200 words"""
        return f'{prompt}: {input}'

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            'post': post,
            'post_tags': post.tag.all(),
            'comment_form': CommentForm(),
            'comments': post.comments.all().order_by('-id'),
            'comlen': len(post.comments.all()),
            'saved_for_later': self.is_stored_post(request, post.id)
        }
        return render(request, 'blog/post-detail.html', context)

    def post(self, request, slug):
        post = Post.objects.get(slug=slug)

        comment_data = {
            'username': request.POST['username'],
            'user_email': request.POST['user_email'],
            'commentByChatGPT': request.POST['commentByChatGPT'], 
            'text': request.POST['commentByChatGPT']
        }

        is_checkbox_enabled_for_comment_generation = comment_data['commentByChatGPT']
        if is_checkbox_enabled_for_comment_generation == 'on':
                chat_gpt_comment = client.completions.create(model="gpt-3.5-turbo",
                prompt=self.generate_prompt_for_openai(post.title),
                temperature=0.6)
                comment_data['text'] = chat_gpt_comment
        
        comment_form = CommentForm(comment_data)
        
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse('post-detail-page', args=[slug]))
        
        context = {
            'post': post,
            'post_tags': post.tag.all(),
            'comment_form': comment_form,
            'comments': post.comments.all().order_by('-id'),
            'comlen': len(post.comments.all()),
            'saved_for_later': self.is_stored_post(request, post.id)
        }
        return render(request, 'blog/post-detail.html', context)
    
class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get('stored_posts')

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context['posts'] = []
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context['posts'] = posts
            context['has_posts'] = True

        return render(request, 'blog/stored-posts.html', context)


    def post(self, request):
        stored_posts = request.session.get('stored_posts')
        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST['post_id'])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
            
        request.session['stored_posts'] = stored_posts

        return HttpResponseRedirect('/')
        # extract the post id from request object
        # add the id in session object
        # request['session'] = post.id