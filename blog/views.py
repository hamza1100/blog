from datetime import date
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post

# all_posts = [
#     {
#         'slug': 'hike-in-the-mountains',
#         'image': 'mountains.jpg',
#         'author': 'Hamza',
#         'date': date(2023, 1, 5),
#         'title': 'Mountain Hiking',
#         'excerpt': 'There\'s nothing like the views you get when hiking in the mountains! And I wasn\'t even prepared for what happened whilst I was enjoying the view!',
#         'content':"""Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
#             Sed sed quam a ex bibendum laoreet sit amet vel arcu. 
#             Donec efficitur elit id elit dapibus ornare. In consequat vulputate nibh, ac tincidunt lacus semper non. 
#             Donec vel tortor ullamcorper, bibendum justo non, congue libero. Sed nisi justo, finibus nec posuere ut, s
#             uscipit sit amet diam. Nullam condimentum gravida mattis.
            
#             Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
#             Sed sed quam a ex bibendum laoreet sit amet vel arcu. 
#             Donec efficitur elit id elit dapibus ornare. In consequat vulputate nibh, ac tincidunt lacus semper non. 
#             Donec vel tortor ullamcorper, bibendum justo non, congue libero. Sed nisi justo, finibus nec posuere ut, s
#             uscipit sit amet diam. Nullam condimentum gravida mattis.
            
#             Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
#             Sed sed quam a ex bibendum laoreet sit amet vel arcu. 
#             Donec efficitur elit id elit dapibus ornare. In consequat vulputate nibh, ac tincidunt lacus semper non. 
#             Donec vel tortor ullamcorper, bibendum justo non, congue libero. Sed nisi justo, finibus nec posuere ut, s
#             uscipit sit amet diam. Nullam condimentum gravida mattis."""
#     },
#     {
#         "slug": "programming-is-fun",
#         "image": "coding.jpg",
#         "author": "Hamza",
#         "date": date(2022, 3, 10),
#         "title": "Programming Is Great!",
#         "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "into-the-woods",
#         "image": "woods.jpg",
#         "author": "Hamza",
#         "date": date(2020, 8, 5),
#         "title": "Nature At Its Best",
#         "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     }
# ]

def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    try:
        all_posts = Post.objects.all().order_by('-date')[:3]
        print('all posts :', all_posts)
        # sorted_posts = sorted(all_posts, key=get_date)
        # latest_posts = sorted_posts[-3:]
        return render(request, "blog/index.html", {
            "posts": all_posts
        })
    except:
        raise Http404()


def posts(request):
    try:
        all_posts = Post.objects.all().order_by('-date')
        return render(request, 'blog/all-posts.html', {
            'all_posts': all_posts
        })
    except:
        raise Http404()

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