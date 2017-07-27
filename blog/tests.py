from django.test import TestCase

from .models import Article


class EntryModelTest(TestCase):
    def test_article(self):
        article = Article(title="My entry title",
                          slug="my-entry-title",
                          sub_title="sub title")
        self.assertEqual(str(article), article.title)
