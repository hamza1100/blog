from django.test import TestCase

from ..models import Post, Comment, Author, Tag

class TestModel(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name='Test First Name',
            last_name='Test Last Name',
            email_address='test@email.com',
        )

        self.tag = Tag.objects.create(
            caption='Test Tag Caption'
        )
        
        self.post = Post.objects.create(
            title='Test Post',
            image=False,
            excerpt='This is a test post',
            slug='test-post',
            content='This is the description of test post added to test the functionality',
            author=self.author
        )

        self.post.tag.add(self.tag)

        self.comment = Comment.objects.create(
            username='Test Username',
            user_email='Test Email',
            text='This is my comment on the post',
            post=self.post
        )

    def test_author_is_created(self):
        self.assertEqual(self.author.first_name, 'Test First Name')
        self.assertEqual(self.author.first_name, 'Test First Name')
        self.assertEqual(self.author.first_name, 'Test First Name')

    def test_tag_is_created(self):
        self.assertEqual(self.tag.caption, 'Test Tag Caption')

    def test_post_is_created(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.tag.get().caption, 'Test Tag Caption')
        self.assertEqual(self.post.author.first_name, 'Test First Name')

    def test_comment_is_created(self):
        self.assertEqual(self.comment.username, 'Test Username')
        self.assertEqual(self.comment.user_email, 'Test Email')
        self.assertEqual(self.comment.post.title, 'Test Post')
