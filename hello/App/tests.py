from django.test import TestCase
from django.urls import resolve
from App.views import home_page
from django.http import HttpRequest
from App.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        # self.assertEqual(1+1,3)
        found=resolve('/')
        self.assertEqual(found.func,home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        # self.assertTemplateUsed(response, 'wrong.html')
        self.assertTemplateUsed(response, 'home.html')