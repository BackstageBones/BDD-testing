from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test author')
        self.assertEqual(b.author, 'Test author')
        self.assertEqual(b.title, 'Test')
        self.assertListEqual(b.posts, [])

    def test_repr(self):
        b = Blog('Test', 'Test author')
        self.assertEqual(b.__repr__(), 'Class Blog initialized with params Test for title, and Test author for author')