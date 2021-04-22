from django.test import TestCase
from django.urls import resolve
from App.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        # self.assertEqual(1+1,3)
        found=resolve('/')
        self.assertEqual(found.func,home_page)