from django.test import SimpleTestCase
from django.urls import reverse

class Snakstest(SimpleTestCase):
    def test_home_page_status(self):
        url=reverse('home')
        respones=self.client.get(url)
        self.assertEqual(respones.status_code,200)
    
    def test_about_page_status(self):
        url=reverse('about')
        respones=self.client.get(url)
        self.assertEqual(respones.status_code,200)
    def test_home_page_template(self):
        url=reverse('home')
        respones=self.client.get(url)
        self.assertTemplateUsed(respones,'home.html')
    def test_about_page_template(self):
        url=reverse('about')
        respones=self.client.get(url)
        self.assertTemplateUsed(respones,'about.html')