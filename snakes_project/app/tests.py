from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.

class TestPages(SimpleTestCase):
    def test_home_status_code(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_about_us_status_code(self):
        url = reverse('about-us')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_home_template(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'home.html')

    def test_about_us_template(self):
        url = reverse('about-us')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'about_us.html')