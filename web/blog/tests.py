from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from .views import list as list_view


class UrlTest(TestCase):

    def test_root_url_resolve_to_list(self):
        found = resolve('/')
        self.assertEqual(found.func, list_view)

    def test_list_return_html(self):
        req = HttpRequest()
        resp = list_view(req)
        # 常量的测试
        self.assertTrue(resp.content.startswith(b'\n<!DOCTYPE html>'))
        self.assertIn(b"<title>Mike's Blog</title>", resp.content)
        self.assertTrue(resp.content.endswith(b'</html>\n'))
        # 实现方式的测试
        expected_html = render_to_string('list.html')
        self.assertEqual(resp.content.decode(), expected_html)
