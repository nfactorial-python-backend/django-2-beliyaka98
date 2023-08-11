from django.test import TestCase
from django.urls import reverse
from .models import New

class TestNewsModel(TestCase):
    def test_has_comments_true(self):
        new = New(title="SOme news", content="from away now day come here")
        new.save()
        new.comment_set.create(content="some comment")
        new.save()
        self.assertGreater(len(new.comment_set.all()), 0)
    def test_has_comments_false(self):
        new = New(title="SOme news", content="from away now day come here")
        new.save()
        self.assertEqual(len(new.comment_set.all()), 0)

class TestNewsViews(TestCase):
    def test_news_view(self):
        new = New(title="Some news", content="from away now day come here")
        new.save()
        new2 = New(title="Same news", content="from away now day come here")
        new2.save()
        new3 = New(title="ALso same news", content="from away now day come here")
        new3.save()

        url = reverse("news")
        response = self.client.get(url)
        self.assertQuerysetEqual([new3, new2, new], response.context["news"])
    
    def test_detail(self):
        new = New(title="Some news", content="from away now day come here")
        new.save()

        url = reverse("detail", args=(new.id,))
        response = self.client.get(url)
        self.assertContains(response, new.title)
        self.assertContains(response, new.content)
    
    def test_detail_comments(self):
        new = New(title="Some news", content="from away now day come here")
        new.save()
        comment1 = new.comment_set.create(content="comment1")
        comment2 = new.comment_set.create(content="comment2")
        new.save()

        url = reverse("detail", args=(new.id,))
        response = self.client.get(url)
        self.assertQuerysetEqual([comment2, comment1], response.context["comments"])