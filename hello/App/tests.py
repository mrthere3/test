from django.test import TestCase
from django.urls import resolve
from App.views import home_page
from django.http import HttpRequest

# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        # self.assertEqual(1+1,3)
        found=resolve('/')
        self.assertEqual(found.func,home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response=home_page(request)
        html = response.content.decode('utf-8') #使用断言 判断返还的html中的文本内容是否含有 我们所要求的的内容
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>',html)
        self.assertTrue(html.endswith('</html>'))