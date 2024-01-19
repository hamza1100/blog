from django.test import TestCase, Client
from django.urls import reverse
from ..models import Post

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('starting-page')
        self.list_all_posts_url = reverse('posts-page')
        self.single_post_url = reverse('post-detail-page', args=['test-post'])

        self.post = Post.objects.create(
            title='Test Post',
            image=False,
            excerpt='This is a test post',
            slug='test-post',
            content='This is the description of test post added to test the functionality',
        ).save()

    def test_start_page_view(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_all_posts_view(self):
        response = self.client.get(self.list_all_posts_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/all-posts.html')

    def test_single_post_view(self):
        response = self.client.get(self.single_post_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post-detail.html')