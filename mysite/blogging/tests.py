from django.test import TestCase
from django.contrib.auth.models import User
from blogging.models import Post, Category

class PostTestCase(TestCase):
    fixtures = ['blogging_test_fixture.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a title"
        self.assertEqual(expected, str(Post(title=expected)))

class CategoryTestCase(TestCase):
    
    def test_string_representation(self):
        expected = "A Category"
        self.assertEqual(expected, str(Category(name=expected)))