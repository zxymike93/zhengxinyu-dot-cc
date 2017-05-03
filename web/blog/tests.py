from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase

from .views import list


class UrlTest(TestCase):

    def test_root_url_resolve_to_list(self):
        found = resolve('/')
        self.assertEqual(found.func, list)

    def test_list_return_html(self):
        req = HttpRequest()
        resp = list(req)
        self.assertTrue(resp.content.startswith(b'\n<!DOCTYPE html>'))
        self.assertIn(b"<title>Mike's Blog</title>", resp.content)
        self.assertTrue(resp.content.endswith(b'</html>\n'))
