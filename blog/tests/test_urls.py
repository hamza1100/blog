from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import AllPostsView, SinglePostView, StartingPageView, ReadLaterView

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('posts-page')
        self.assertEqual(resolve(url).func.view_class, AllPostsView)

    def test_starging_page_url_is_resolved(self):
        url = reverse('starting-page')
        self.assertEqual(resolve(url).func.view_class, StartingPageView)

    def test_read_later_url_is_resolved(self):
        url = reverse('read-later')
        self.assertEqual(resolve(url).func.view_class, ReadLaterView)

    def test_post_detail_page_url_is_resolved(self):
        url = reverse('post-detail-page', args=['post-slug'])
        self.assertEqual(resolve(url).func.view_class, SinglePostView)
