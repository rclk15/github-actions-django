from django.test import TestCase

# this includes the python test framework

from .models import Post


class ModelTesting(TestCase):
    def setUp(self):
        # object is default model manager
        self.blog = Post.objects.create(
            title="first blog", author="ricky", slug="first_blog"
        )

    def test_post_model(self):
        d = self.blog
        # make sure data matches description
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), "first blog")
